"""Custom tools that provide fixed proverb data for Japanese and global lists."""

from __future__ import annotations

from typing import Any, Iterable, Sequence

from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.tool_configs import ToolArgsConfig


_JAPANESE_PROVERBS: tuple[dict[str, Any], ...] = (
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
    {
        "proverb": "石橋を叩いて渡る",
        "reading": "いしばしをたたいてわたる",
        "meaning": "Tap the stone bridge before crossing: double-check before acting.",
        "themes": ("risk", "due diligence", "planning"),
        "usage_hint": "When caution or verification is the main advice.",
    },
    {
        "proverb": "猿も木から落ちる",
        "reading": "さるもきからおちる",
        "meaning": "Even monkeys fall from trees: experts still make mistakes.",
        "themes": ("humility", "failure", "learning"),
        "usage_hint": "Use to calm someone who slipped up despite expertise.",
    },
    {
        "proverb": "雨降って地固まる",
        "reading": "あめふってじかたまる",
        "meaning": "After rain, the ground hardens: conflict can strengthen bonds.",
        "themes": ("conflict", "relationships", "team"),
        "usage_hint": "Good when smoothing over drama or setbacks.",
    },
    {
        "proverb": "花より団子",
        "reading": "はなよりだんご",
        "meaning": "Dumplings over flowers: practicality beats aesthetics.",
        "themes": ("pragmatism", "budget", "events"),
        "usage_hint": "Use when someone must choose usefulness over looks.",
    },
    {
        "proverb": "塵も積もれば山となる",
        "reading": "ちりもつもればやまとなる",
        "meaning": "Dust piles up into mountains: small efforts accumulate.",
        "themes": ("habits", "savings", "practice"),
        "usage_hint": "Motivate steady incremental progress.",
    },
    {
        "proverb": "柳に風",
        "reading": "やなぎにかぜ",
        "meaning": "Wind through a willow: flexibility prevents breakage.",
        "themes": ("adaptability", "stress", "negotiation"),
        "usage_hint": "Suggest bending instead of snapping during change.",
    },
    {
        "proverb": "腹八分目に医者いらず",
        "reading": "はらはちぶんめにいしゃいらず",
        "meaning": "Stop eating at eighty percent: moderation keeps you healthy.",
        "themes": ("health", "discipline", "balance"),
        "usage_hint": "Great for lifestyle or burnout discussions.",
    },
    {
        "proverb": "灯台下暗し",
        "reading": "とうだいもとくらし",
        "meaning": "It is dark under the lighthouse: you miss what's close by.",
        "themes": ("awareness", "investigation", "team"),
        "usage_hint": "When the answer is nearby but overlooked.",
    },
    {
        "proverb": "石の上の水も三年",
        "reading": "いしのうえのみずもさんねん",
        "meaning": "Even water on a stone takes three years: persistence changes anything.",
        "themes": ("patience", "habits", "long-term"),
        "usage_hint": "Emphasize long-haul dedication.",
    },
    {
        "proverb": "馬の耳に念仏",
        "reading": "うまのみみにねんぶつ",
        "meaning": "Chanting sutras to a horse: advice ignored falls flat.",
        "themes": ("communication", "feedback", "team"),
        "usage_hint": "When someone's warnings are being ignored.",
    },
    {
        "proverb": "覆面の下は笑っている",
        "reading": "ふくめんのしたはわらっている",
        "meaning": "Behind the mask there is a grin: hidden motives exist.",
        "themes": ("politics", "office", "trust"),
        "usage_hint": "Use for navigating subtle workplace dynamics.",
    },
    {
        "proverb": "泣きっ面に蜂",
        "reading": "なきっつらにはち",
        "meaning": "Bees sting a crying face: misfortunes pile up.",
        "themes": ("bad luck", "resilience", "emotions"),
        "usage_hint": "For times when everything goes wrong at once.",
    },
    {
        "proverb": "船頭多くして船山に登る",
        "reading": "せんどうおおくしてふねやまにのぼる",
        "meaning": "Too many captains steer the boat up a mountain: too many leaders ruin plans.",
        "themes": ("leadership", "projects", "alignment"),
        "usage_hint": "When collaboration lacks a clear owner.",
    },
    {
        "proverb": "聞くは一時の恥、聞かぬは一生の恥",
        "reading": "きくはいっときのはじ、きかぬはいっしょうのはじ",
        "meaning": "Asking once is momentary shame; not asking is lifelong shame.",
        "themes": ("learning", "mentorship", "courage"),
        "usage_hint": "Encourage questions or seeking help.",
    },
    {
        "proverb": "短気は損気",
        "reading": "たんきはそんき",
        "meaning": "Short temper, short fortune: impatience costs you.",
        "themes": ("emotions", "negotiation", "leadership"),
        "usage_hint": "Use when cooling someone down.",
    },
)

_GLOBAL_PROVERBS: tuple[dict[str, Any], ...] = (
    {
        "proverb": "When in Rome, do as the Romans do",
        "origin": "Italy",
        "meaning": "Adapting to local customs prevents friction.",
        "themes": ("culture", "travel", "team"),
        "usage_hint": "Use when someone must respect an existing process.",
    },
    {
        "proverb": "A stitch in time saves nine",
        "origin": "England",
        "meaning": "Fixing small issues early prevents bigger messes.",
        "themes": ("maintenance", "planning", "quality"),
        "usage_hint": "Encourage proactive action before things blow up.",
    },
    {
        "proverb": "The squeaky wheel gets the grease",
        "origin": "United States",
        "meaning": "Those who speak up receive attention first.",
        "themes": ("advocacy", "priorities", "communication"),
        "usage_hint": "Good when nudging someone to ask for support.",
    },
    {
        "proverb": "Measure twice, cut once",
        "origin": "Carpentry proverb",
        "meaning": "Preparation avoids costly rework.",
        "themes": ("craftsmanship", "planning", "quality"),
        "usage_hint": "Use for launches or irreversible decisions.",
    },
    {
        "proverb": "Empty barrels make the most noise",
        "origin": "Ireland",
        "meaning": "Loud bragging often hides lack of substance.",
        "themes": ("ego", "leadership", "focus"),
        "usage_hint": "When dealing with performative teammates.",
    },
    {
        "proverb": "Better an egg today than a hen tomorrow",
        "origin": "Spain",
        "meaning": "A small sure thing beats a big maybe.",
        "themes": ("negotiation", "finance", "risk"),
        "usage_hint": "Encourage cashing in guaranteed wins.",
    },
    {
        "proverb": "He who chases two rabbits catches neither",
        "origin": "Russia",
        "meaning": "Split attention ruins both goals.",
        "themes": ("focus", "projects", "strategy"),
        "usage_hint": "Parallel to Japanese rabbit proverb; use for prioritization.",
    },
    {
        "proverb": "No bees, no honey; no work, no money",
        "origin": "French",
        "meaning": "Rewards require effort.",
        "themes": ("work", "motivation", "finance"),
        "usage_hint": "Remind someone that grind precedes payoff.",
    },
    {
        "proverb": "The best time to plant a tree was twenty years ago. The second best time is now",
        "origin": "Chinese",
        "meaning": "Late action still beats inaction.",
        "themes": ("long-term", "habits", "personal growth"),
        "usage_hint": "Use when someone regrets procrastinating.",
    },
    {
        "proverb": "Trust, but verify",
        "origin": "Russian (popularized in US)",
        "meaning": "Believe people, yet confirm the facts.",
        "themes": ("governance", "security", "partnerships"),
        "usage_hint": "Great for audits or vendor oversight.",
    },
    {
        "proverb": "Little by little, the bird builds its nest",
        "origin": "Haitian",
        "meaning": "Small consistent steps create big outcomes.",
        "themes": ("habits", "learning", "projects"),
        "usage_hint": "Motivate incremental work when the goal is huge.",
    },
    {
        "proverb": "You can't plow a field by turning it over in your mind",
        "origin": "Ireland",
        "meaning": "Thinking alone changes nothing; act.",
        "themes": ("procrastination", "action", "projects"),
        "usage_hint": "Perfect when analysis paralysis strikes.",
    },
    {
        "proverb": "Fall seven times, stand up eight",
        "origin": "Japanese via English",
        "meaning": "Resilience beats perfection.",
        "themes": ("perseverance", "motivation", "sports"),
        "usage_hint": "Globalized twin to 七転び八起き.",
    },
    {
        "proverb": "Even a fish wouldn't get into trouble if it kept its mouth shut",
        "origin": "Polish",
        "meaning": "Sometimes silence is safer.",
        "themes": ("gossip", "meetings", "risk"),
        "usage_hint": "Use when over-sharing causes problems.",
    },
    {
        "proverb": "Smooth seas do not make skillful sailors",
        "origin": "African",
        "meaning": "Challenge is required for mastery.",
        "themes": ("growth", "training", "resilience"),
        "usage_hint": "Help someone embrace a rough sprint or launch.",
    },
    {
        "proverb": "If you want to go fast, go alone; if you want to go far, go together",
        "origin": "African",
        "meaning": "Teamwork extends reach even if it slows pace.",
        "themes": ("collaboration", "leadership", "strategy"),
        "usage_hint": "Use when debating solo vs. team effort.",
    },
    {
        "proverb": "The camel cannot see its own hump",
        "origin": "Arab",
        "meaning": "People miss their own flaws.",
        "themes": ("feedback", "self-awareness", "mentorship"),
        "usage_hint": "For coaching conversations.",
    },
    {
        "proverb": "You reap what you sow",
        "origin": "Biblical",
        "meaning": "Consequences match the effort invested.",
        "themes": ("accountability", "karma", "habits"),
        "usage_hint": "Classic warning that shortcuts come back around.",
    },
)


def _keyword_hit(text: str, keywords: Iterable[str]) -> bool:
    lowered = text.casefold()
    return any(keyword in lowered for keyword in keywords if keyword)


def _filter_proverbs(dataset: Sequence[dict[str, Any]], theme: str) -> list[dict[str, Any]]:
    results = list(dataset)
    normalized_theme = (theme or "").strip()
    if not normalized_theme:
        return results

    normalized = normalized_theme.replace("\u3000", " ").casefold()
    tokens = tuple(token for token in normalized.split() if token)
    keywords = tokens or (normalized,)
    filtered: list[dict[str, Any]] = []
    for proverb in results:
        haystacks = (
            proverb.get("proverb", ""),
            proverb.get("reading", ""),
            proverb.get("meaning", ""),
            " ".join(proverb.get("themes", ()) or ()),
            proverb.get("origin", ""),
            proverb.get("usage_hint", ""),
        )
        if any(_keyword_hit(haystack, keywords) for haystack in haystacks if haystack):
            filtered.append(proverb)

    return filtered or results


def _get_japanese_proverb_list(theme: str = "") -> dict[str, Any]:
    """Return a curated set of Japanese proverbs relevant to a theme."""

    matches = _filter_proverbs(_JAPANESE_PROVERBS, theme)
    return {"proverbs": matches, "count": len(matches)}


def _get_global_proverb_list(theme: str = "") -> dict[str, Any]:
    """Return a curated set of non-Japanese proverb data."""

    matches = _filter_proverbs(_GLOBAL_PROVERBS, theme)
    return {"proverbs": matches, "count": len(matches)}


def get_japanese_proverb_list_tool(args: ToolArgsConfig) -> FunctionTool:
    """Factory used from YAML to expose the Japanese proverb list."""

    require_confirmation = bool(getattr(args, "require_confirmation", False))

    return FunctionTool(
        _get_japanese_proverb_list,
        require_confirmation=require_confirmation,
    )


def get_global_proverb_list_tool(args: ToolArgsConfig) -> FunctionTool:
    """Factory used from YAML to expose the global proverb list."""

    require_confirmation = bool(getattr(args, "require_confirmation", False))

    return FunctionTool(
        _get_global_proverb_list,
        require_confirmation=require_confirmation,
    )
