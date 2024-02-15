def battle_run(damage, defence, mods_sum):
    hp = (defence['hp'] + 65) * defence['level']/50 + 10
    defence_def = (defence['defence'] + 46.875) * defence['level']/50 + 5
    attack = (damage['attack'] + 46.875) * damage['level']/50 + 5
    damageMin = (((2* damage['level']/5 + 2) * attack * damage['move_power'] /defence_def)/50 * 85 / 100 + 2) * mods_sum
    atk_speed = damage['speed']
    def_speed = defence['speed']
    if damageMin > hp and atk_speed > def_speed:
        # print(f'{damageMin} damage is enough to outspeed & KO the defending pokemon')
        return 1
    else:
        # print(f'{damageMin} damage is not enough to outspeed & KO the defending pokemon')
        return 0