def battle_run(damage, defence, mods_sum):
    hp = (defence['hp'] + 65) * defence['level']/50 + 10
    defence_def = (defence['defence'] + 46.875) * defence['level']/50 + 5
    attack = (damage['attack'] + 46.875) * damage['level']/50 + 5
    damageMin = (((2* damage['level']/5 + 2) * attack * damage['move_power'] /defence_def)/50 * 85 / 100 + 2) * mods_sum
    if damageMin > hp:
        print(f'{damageMin} damage is enough to KO the defending pokemon')
        return 1
    else:
        print(f'{damageMin} damage is not enough to KO the defending pokemon')
        return 0