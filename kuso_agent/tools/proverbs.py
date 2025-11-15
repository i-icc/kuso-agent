"""Custom tools that provide fixed proverb + idiom data for kuso_agent."""

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

_YOJIJUKUGO: tuple[dict[str, Any], ...] = (
    {
        "idiom": "起死回生",
        "reading": "きしかいせい",
        "meaning": "一度ダメになった状況を根性で立て直すこと。",
        "themes": ("recovery", "motivation", "projects"),
        "usage_hint": "大逆転やV字回復を狙う時に。",
    },
    {
        "idiom": "四面楚歌",
        "reading": "しめんそか",
        "meaning": "周囲が全部敵で味方ゼロの孤立状態。",
        "themes": ("politics", "team", "stress"),
        "usage_hint": "孤軍奮闘している相談者向け。",
    },
    {
        "idiom": "臥薪嘗胆",
        "reading": "がしんしょうたん",
        "meaning": "屈辱を忘れず努力してリベンジを狙うこと。",
        "themes": ("career", "revenge", "training"),
        "usage_hint": "悔しさを原動力にしている相手へ。",
    },
    {
        "idiom": "電光石火",
        "reading": "でんこうせっか",
        "meaning": "電撃のように素早く動くさま。",
        "themes": ("speed", "decisions", "ops"),
        "usage_hint": "判断や行動を急ぎたい時に。",
    },
    {
        "idiom": "暗中模索",
        "reading": "あんちゅうもさく",
        "meaning": "何も見えない状況で手探りを続けること。",
        "themes": ("uncertainty", "product", "research"),
        "usage_hint": "方向性を迷っている場面に。",
    },
    {
        "idiom": "粉骨砕身",
        "reading": "ふんこつさいしん",
        "meaning": "骨を粉にするほど全力を尽くすこと。",
        "themes": ("effort", "loyalty", "team"),
        "usage_hint": "無茶な頑張りを美談にしたい時。",
    },
    {
        "idiom": "朝令暮改",
        "reading": "ちょうれいぼかい",
        "meaning": "朝の命令が夕方には変わるほど方針がぐらつくさま。",
        "themes": ("management", "chaos", "planning"),
        "usage_hint": "上層部の迷走をいじる時に。",
    },
    {
        "idiom": "自業自得",
        "reading": "じごうじとく",
        "meaning": "自分の行いの結果を自分が受けること。",
        "themes": ("accountability", "karma", "discipline"),
        "usage_hint": "自爆した人へ辛口コメントする時。",
    },
    {
        "idiom": "有言実行",
        "reading": "ゆうげんじっこう",
        "meaning": "口にしたことをきっちり実行するさま。",
        "themes": ("integrity", "leadership", "habits"),
        "usage_hint": "やると言った人を追い込むとき。",
    },
    {
        "idiom": "一石二鳥",
        "reading": "いっせきにちょう",
        "meaning": "一つの行動で二つの成果を得ること。",
        "themes": ("efficiency", "strategy", "tradeoff"),
        "usage_hint": "一挙両得を狙う相談に。",
    },
    {
        "idiom": "右往左往",
        "reading": "うおうさおう",
        "meaning": "混乱して行ったり来たりするさま。",
        "themes": ("panic", "ops", "communication"),
        "usage_hint": "現場がバタついている話題に。",
    },
    {
        "idiom": "単刀直入",
        "reading": "たんとうちょくにゅう",
        "meaning": "遠回しにせず核心をズバッと言うこと。",
        "themes": ("communication", "feedback", "leadership"),
        "usage_hint": "はっきり物を言いたい人向け。",
    },
    {
        "idiom": "泰然自若",
        "reading": "たいぜんじじゃく",
        "meaning": "大物のように落ち着き払っているさま。",
        "themes": ("mindset", "stress", "presence"),
        "usage_hint": "慌てない姿勢をすすめる時。",
    },
    {
        "idiom": "以心伝心",
        "reading": "いしんでんしん",
        "meaning": "言葉がなくても心が伝わること。",
        "themes": ("team", "relationships", "collaboration"),
        "usage_hint": "空気で察しろ案件に。",
    },
    {
        "idiom": "適材適所",
        "reading": "てきざいてきしょ",
        "meaning": "才能に合わせて役割を割り振ること。",
        "themes": ("management", "hiring", "team"),
        "usage_hint": "人員配置の話で使いやすい。",
    },
    {
        "idiom": "公私混同",
        "reading": "こうしこんどう",
        "meaning": "公的な事と私事を混ぜてしまうこと。",
        "themes": ("ethics", "leadership", "governance"),
        "usage_hint": "利害がぐちゃぐちゃな人向け。",
    },
    {
        "idiom": "自由奔放",
        "reading": "じゆうほんぽう",
        "meaning": "好き勝手に振る舞うさま。",
        "themes": ("creativity", "culture", "personality"),
        "usage_hint": "縛られたくない人をヨイショする時。",
    },
    {
        "idiom": "不眠不休",
        "reading": "ふみんふきゅう",
        "meaning": "眠らず休まず働き続けること。",
        "themes": ("burnout", "dedication", "ops"),
        "usage_hint": "社畜ノリを自虐するのに便利。",
    },
    {
        "idiom": "面従腹背",
        "reading": "めんじゅうふくはい",
        "meaning": "表面上は従いながら内心では逆らうこと。",
        "themes": ("politics", "compliance", "trust"),
        "usage_hint": "上司に従うふりをしている状況に。",
    },
    {
        "idiom": "傍若無人",
        "reading": "ぼうじゃくぶじん",
        "meaning": "周りの迷惑を無視してやりたい放題するさま。",
        "themes": ("ego", "leadership", "conflict"),
        "usage_hint": "暴走気味の人をいじる時。",
    },
    {
        "idiom": "付和雷同",
        "reading": "ふわらいどう",
        "meaning": "自分の意見を持たず周囲に合わせること。",
        "themes": ("consensus", "politics", "team"),
        "usage_hint": "流されやすいメンバーに皮肉を言う時。",
    },
    {
        "idiom": "異口同音",
        "reading": "いくどうおん",
        "meaning": "みんなが同じことを口にすること。",
        "themes": ("alignment", "team", "culture"),
        "usage_hint": "全員一致ムードを強調する話題に。",
    },
    {
        "idiom": "千載一遇",
        "reading": "せんざいいちぐう",
        "meaning": "千年に一度レベルの貴重なチャンス。",
        "themes": ("opportunity", "timing", "risk"),
        "usage_hint": "絶好の機会を逃したくない時。",
    },
    {
        "idiom": "心機一転",
        "reading": "しんきいってん",
        "meaning": "気分を新たにして仕切り直すこと。",
        "themes": ("reset", "career", "habits"),
        "usage_hint": "再スタートしたい場面に。",
    },
    {
        "idiom": "老若男女",
        "reading": "ろうにゃくなんにょ",
        "meaning": "老いも若きも男女も。あらゆる人。",
        "themes": ("audience", "community", "diversity"),
        "usage_hint": "全方位巻き込み案件で便利。",
    },
    {
        "idiom": "内憂外患",
        "reading": "ないゆうがいかん",
        "meaning": "内側にも外側にも問題を抱えること。",
        "themes": ("strategy", "risk", "politics"),
        "usage_hint": "課題だらけの状態を嘆く時。",
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
            proverb.get("idiom", ""),
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


def _get_yojijukugo_list(theme: str = "") -> dict[str, Any]:
    """Return four-character idioms that roughly match a theme."""

    matches = _filter_proverbs(_YOJIJUKUGO, theme)
    return {"idioms": matches, "count": len(matches)}


def get_japanese_proverb_list_tool(args: ToolArgsConfig) -> FunctionTool:
    """Factory used from YAML to expose the Japanese proverb list."""

    require_confirmation = bool(getattr(args, "require_confirmation", False))

    return FunctionTool(
        _get_japanese_proverb_list,
        require_confirmation=require_confirmation,
    )


def get_yojijukugo_list_tool(args: ToolArgsConfig) -> FunctionTool:
    """Factory used from YAML to expose the 四字熟語 list."""

    require_confirmation = bool(getattr(args, "require_confirmation", False))

    return FunctionTool(
        _get_yojijukugo_list,
        require_confirmation=require_confirmation,
    )
