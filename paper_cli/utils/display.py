"""Rich display utilities for paper CLI."""

from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

if TYPE_CHECKING:
    from ..core.models import Paper


console = Console()


def display_papers_table(
    papers: List["Paper"],
    title: str = "Papers",
    show_all: bool = False
) -> None:
    """
    以表格形式显示论文列表。

    Args:
        papers: 论文列表
        title: 表格标题
        show_all: 是否显示所有字段
    """
    if not papers:
        console.print("[yellow]No papers found.[/yellow]")
        return

    table = Table(title=title, show_lines=True)

    # 基本列
    table.add_column("#", style="dim", width=4)
    table.add_column("Title", style="cyan", max_width=50)
    table.add_column("Tags", style="green", max_width=30)
    # Show IMWUT volume/issue for UbiComp papers (journal-style continuous issues).
    table.add_column("Source", style="magenta", max_width=32)

    if show_all:
        table.add_column("Authors", max_width=25)
        table.add_column("Topic", style="blue")
        table.add_column("Date")

    for i, paper in enumerate(papers, 1):
        # 截断过长的标题
        title_display = paper.title[:47] + "..." if len(paper.title) > 50 else paper.title

        source_display = paper.source
        if paper.journal_ref and paper.journal_ref.strip().startswith("IMWUT"):
            source_display = f"{paper.source} ({paper.journal_ref.strip()})"

        if show_all:
            table.add_row(
                str(i),
                title_display,
                paper.tag,
                source_display,
                paper.authors,
                paper.topic,
                paper.date
            )
        else:
            table.add_row(
                str(i),
                title_display,
                paper.tag,
                source_display
            )

    console.print(table)


def display_paper_detail(paper: "Paper") -> None:
    """显示单篇论文的详细信息。"""
    content = f"""[bold]Title:[/bold] {paper.title}
[bold]Authors:[/bold] {paper.authors or 'N/A'}
[bold]Source:[/bold] {paper.source or 'N/A'}
[bold]Topic:[/bold] {paper.topic}
[bold]Tags:[/bold] {paper.tag or 'N/A'}
[bold]Subjects:[/bold] {paper.subjects or 'N/A'}
[bold]Link:[/bold] {paper.link}
[bold]Date:[/bold] {paper.date or 'N/A'}
[bold]DOI:[/bold] {paper.doi or 'N/A'}
[bold]Journal Ref:[/bold] {paper.journal_ref or 'N/A'}"""

    if paper.additional_info:
        content += f"\n[bold]Comment/Notes:[/bold] {paper.additional_info}"

    console.print(Panel(content, title="Paper Details", expand=False))


def display_topics(topics: dict) -> None:
    """显示 topics 统计。"""
    table = Table(title="Topics")
    table.add_column("Topic", style="cyan")
    table.add_column("Count", justify="right", style="green")
    table.add_column("Percentage", justify="right")

    total = sum(topics.values())
    for topic, count in topics.items():
        pct = f"{count / total * 100:.1f}%"
        table.add_row(topic, str(count), pct)

    table.add_section()
    table.add_row("[bold]Total[/bold]", f"[bold]{total}[/bold]", "100%")

    console.print(table)


def display_stats(
    total: int,
    topics: dict,
    tags: dict,
    date_range: tuple
) -> None:
    """显示统计信息。"""
    console.print(Panel("[bold]Paper Library Statistics[/bold]", expand=False))

    # 总数
    console.print(f"\n[bold]Total papers:[/bold] {total}")

    # Topics
    console.print(f"\n[bold]Topics:[/bold] {len(topics)}")
    for topic, count in topics.items():
        pct = count / total * 100 if total > 0 else 0
        console.print(f"  • {topic}: {count} ({pct:.1f}%)")

    # Top tags
    console.print(f"\n[bold]Top tags:[/bold]")
    for tag, count in list(tags.items())[:10]:
        console.print(f"  • {tag}: {count}")

    # Date range
    if date_range[0] and date_range[1]:
        console.print(f"\n[bold]Date range:[/bold] {date_range[0]} - {date_range[1]}")


def print_success(message: str) -> None:
    """打印成功消息。"""
    console.print(f"[green]✓[/green] {message}")


def print_error(message: str) -> None:
    """打印错误消息。"""
    console.print(f"[red]✗[/red] {message}")


def print_warning(message: str) -> None:
    """打印警告消息。"""
    console.print(f"[yellow]![/yellow] {message}")


def print_info(message: str) -> None:
    """打印信息消息。"""
    console.print(f"[blue]→[/blue] {message}")
