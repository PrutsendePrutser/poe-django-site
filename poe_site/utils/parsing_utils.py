import re


def parse_affixes(item_from_clipboard):

    # Find explicit mods
    item_properties_start = item_from_clipboard.rfind('--------') + 8

    # Check if it's a unique item
    if item_from_clipboard.startswith("Rarity: Unique"):
        print "Fuck off retard noobshit, not going to do this."
        unique_item_without_flavour_text = item_from_clipboard[:item_properties_start-8].strip()
        explicit_mods_start = unique_item_without_flavour_text.rfind('--------') + 8
        explicit_mods = unique_item_without_flavour_text[explicit_mods_start:].strip().split('\n')
    # Non-unique item
    else:
        explicit_mods = item_from_clipboard[item_properties_start:].strip().split('\n')

    # Remove whitespace
    cleaned_explicit_mods = [mod.strip() for mod in explicit_mods]
    print cleaned_explicit_mods
    # affix_regex = re.compile('\D*\d{1,3}\D+')
    item_affix_dict = {}

    for mod in cleaned_explicit_mods:
        # Find the numeric value in mod
        hit = re.findall('\d{1,3}', mod)

        # Skip things without numeric values, these mods are static
        if not hit:
            continue

        # Get the first numeric value
        val = hit[0]

        # Get the description line, in the same format as the PoE site
        affix_description = mod.replace(val, '#')

        # Store affix, with value
        item_affix_dict[affix_description] = val

    print item_affix_dict

parse_affixes("""Rarity: Unique
Solaris Lorica
Copper Plate
--------
Armour: 222 (augmented)
--------
Requirements:
Level: 17
Str: 53
--------
Sockets: R-R R
--------
Item Level: 73
--------
+14 to Strength
76% increased Armour
25% increased Light Radius
Chaos Damage does not bypass Energy Shield
-10 Chaos Damage taken
--------
Give me neither havens nor solace;
They are for the weak and frightened.
Instead, light the path to greatness,
So that I may begin my bright pursuit.
""")
