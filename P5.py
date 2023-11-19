def power_equiv(watt):
    hp = pwatt/745.7
    btum = pwatt/0.293
    calm = pwatt*14.33
    erg = pwatt*1e7
    flbm = pwatt*44.25
    return hp, btum, calm, erg, flbm

if __name__ == '__main__':
    pwatt = 100
    horsep, btuh, calmin, perg, footlbm = power_equiv(pwatt)
    print(pwatt, 'w =', round(horsep,3), 'hp =',
        round(btuh,3), 'btu/h =',
        round(calmin,3),'cal/min =',
        round(perg,3), 'erg =',
        round(footlbm,3), 'f-lb/min')