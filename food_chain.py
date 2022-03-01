from dataclasses import dataclass
@dataclass
class Animal:
    name: str
    tag_line: str
    swallow_optional: str = ""
ANIMALS = (
    Animal(name="fly", tag_line=""),
    Animal(name="spider",
        tag_line="It wriggled and jiggled and tickled inside her.",
        swallow_optional=" that wriggled and jiggled and tickled inside her."),
    Animal(name="bird", tag_line="How absurd to swallow a bird!"),
    Animal(name="cat", tag_line="Imagine that, to swallow a cat!"),
    Animal(name="dog", tag_line="What a hog, to swallow a dog!"),
    Animal(name="goat", tag_line="Just opened her throat and swallowed a goat!"),
    Animal(name="cow", tag_line="I don't know how she swallowed a cow!"),
    Animal(name="horse", tag_line="She's dead, of course!"),
)
VERSE_OPEN_FORMAT = "I know an old lady who swallowed a {animal}."
VERSE_SWALLOW_FORMAT = "She swallowed the {animal2} to catch the {animal1}{extra}"
VERSE_END = "I don't know why she swallowed the fly. Perhaps she'll die."
def recite(start_verse, end_verse):
    verses = []
    for idx in range(start_verse-1, end_verse):
        verses.extend(verse(idx))
        if idx < end_verse - 1:
            verses.append("")
    return verses
def verse(idx):
    lines = [VERSE_OPEN_FORMAT.format(animal=ANIMALS[idx].name)]
    if ANIMALS[idx].tag_line != "":
        lines.append(ANIMALS[idx].tag_line)
    if idx != len(ANIMALS) - 1:
        for i in range(idx, 0, -1):
            extra = ANIMALS[i-1].swallow_optional \
                if idx > 1 and ANIMALS[i-1].swallow_optional != "" else "."
            lines.append(
                VERSE_SWALLOW_FORMAT.format(
                    animal2=ANIMALS[i].name, animal1=ANIMALS[i-1].name, extra=extra))
        lines.append(VERSE_END)
    return lines
