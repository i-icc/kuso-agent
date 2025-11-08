"""Custom tools that provide fixed Japanese proverb data."""

from __future__ import annotations

from typing import Any
from typing import Iterable

from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.tool_configs import ToolArgsConfig


_PROVERBS: tuple[dict[str, Any], ...] = (
    {
        "proverb": "石の上にも三年",
        "reading": "いしのうえにもさんねん",
        "meaning": "Cold stones warm after three years: patient effort eventually pays off.",
        "themes": ("perseverance", "career", "study"),
        "usage_hint": "Use when encouraging someone to keep grinding even when results feel slow.",
    },
    {
        "proverb": "案ずるより産むが易し",
        "reading": "あんずるよりうむがやすし",
        "meaning": "Doing is easier than worrying: action is simpler than endless anxiety.",
        "themes": ("anxiety", "decisions", "projects"),
        "usage_hint": "Good for someone overthinking a decision or launch.",
    },
    {
        "proverb": "二兎を追う者は一兎をも得ず",
        "reading": "にとをおうものはいっとをもえず",
        "meaning": "Chasing two rabbits nets none: split focus fails both goals.",
        "themes": ("prioritization", "work", "study"),
        "usage_hint": "Use when someone is juggling too many tasks at once.",
    },
    {
        "proverb": "覆水盆に返らず",
        "reading": "ふくすいぼんにかえらず",
        "meaning": "Spilt water never returns to the bowl: irreversible actions stay irreversible.",
        "themes": ("regret", "relationships", "apology"),
        "usage_hint": "For regret or when someone wishes to undo a mistake.",
    },
    {
        "proverb": "七転び八起き",
        "reading": "ななころびやおき",
        "meaning": "Fall seven times, rise eight: resilience is more important than perfection.",
        "themes": ("resilience", "motivation", "health"),
        "usage_hint": "When someone needs morale after repeated setbacks.",
    },
    {
        "proverb": "急がば回れ",
        "reading": "いそがばまわれ",
        "meaning": "When in a hurry, take the long way around: rushing causes delays.",
        "themes": ("quality", "deadlines", "planning"),
        "usage_hint": "Best for people tempted to cut critical corners.",
    },
    {
        "proverb": "初心忘るべからず",
        "reading": "しょしんわするべからず",
        "meaning": "Never forget your beginner's mindset or original intention.",
        "themes": ("growth", "craft", "leadership"),
        "usage_hint": "Helps when someone drifts away from their motivations.",
    },
    {
        "proverb": "情けは人の為ならず",
        "reading": "なさけはひとのためならず",
        "meaning": "Kindness returns to the giver eventually.",
        "themes": ("relationships", "team", "community"),
        "usage_hint": "Use for collaboration or favor fatigue.",
    },
    {
        "proverb": "虎穴に入らずんば虎子を得ず",
        "reading": "こけつにいらずんばこじをえず",
        "meaning": "No tiger cubs without entering the tiger's den: rewards need courage.",
        "themes": ("risk", "entrepreneurship", "career"),
        "usage_hint": "For someone afraid to take a bold step.",
    },
    {
        "proverb": "朱に交われば赤くなる",
        "reading": "しゅにまじわればあかくなる",
        "meaning": "People become like the company they keep.",
        "themes": ("environment", "habits", "relationships"),
        "usage_hint": "Use when warning about influence of peers or co-workers.",
    },
)


def _keyword_hit(text: str, keywords: Iterable[str]) -> bool:
    lowered = text.casefold()
    return any(keyword in lowered for keyword in keywords if keyword)


def _get_japanese_proverb_list(theme: str = "") -> dict[str, Any]:
    """Return a curated set of Japanese proverbs relevant to a theme.

    Args:
        theme: Optional free-form text describing the user's situation. If set,
          the tool filters the proverb list by matching the text against each
          proverb's metadata; otherwise all proverbs are returned.

    Returns:
        Dictionary with the matching proverbs and helper metadata so the agent
        can cite and explain them.
    """
    results = list(_PROVERBS)
    normalized_theme = (theme or "").strip()
    if normalized_theme:
      normalized = normalized_theme.replace('\u3000', ' ').casefold()
      tokens = tuple(token for token in normalized.split() if token)
      keywords = tokens or (normalized,)
      filtered = [
          proverb
          for proverb in results
          if _keyword_hit(proverb["proverb"], keywords)
          or _keyword_hit(proverb["meaning"], keywords)
          or _keyword_hit(" ".join(proverb.get("themes", ())), keywords)
      ]
      if filtered:
        results = filtered

    return {"proverbs": results, "count": len(results)}


def get_japanese_proverb_list_tool(args: ToolArgsConfig) -> FunctionTool:
    """Factory used from YAML to expose the proverb list as a FunctionTool."""

    require_confirmation = bool(getattr(args, "require_confirmation", False))

    return FunctionTool(
        _get_japanese_proverb_list,
        require_confirmation=require_confirmation,
    )
