import json

add_words = """Harry/hairy
whirl/whorl
heels/heals
Lea/lee
who/hoo
carols/carrels
peels/peals
Mae/may
Taylor/tailor
creaks/creeks
tracks/tracts
stairs/stares
Moe/mow
sewing/sowing
Barry/bury
waiting/weighting
Barry/bury
bury/berry
berry/Barry"""

final_dict = dict()
with open('homophone-list.json', mode='r') as f:
    s = f.read()
    old_dict = json.loads(s)

    new_dict = dict()
    new_words = add_words.split('\n')

    for item in new_words:
        tmp = item.split('/')
        new_dict[tmp[0]] = tmp[1]

    united = dict(old_dict, **new_dict)

    print(united)

    for i in sorted(united, key=str.lower):
        final_dict[i] = united[i]

    print(final_dict)

with open('final_list.json', mode='w') as f:
    final_json_str = json.dumps(final_dict)

    f.write(final_json_str)
