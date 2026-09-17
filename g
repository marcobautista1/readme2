'''
Marco Anton S. Bautista
9-Balingkilat
'''
year=int(input("Enter your birth year: "))
if year>=1900:
    byear=year-1900
    bbyear=byear%12
    bbbyear=bbyear+1
    if bbbyear==1:
        print("\nYour Chinese Zodiac Sign is : Rat (鼠 / Shǔ)")
    elif bbbyear==2:
        print("\nYour Chinese Zodiac Sign is : Ox (牛 / Niú)")
    elif bbbyear==3:
        print("\nYour Chinese Zodiac Sign is : Tiger (虎 / Hǔ)")
    elif bbbyear==4:
        print("\nYour Chinese Zodiac Sign is : Rabbit (兔 / Tù)")
    elif bbbyear==5:
        print("\nYour Chinese Zodiac Sign is : Dragon (龙 / Lóng)")
    elif bbbyear==6:
        print("\nYour Chinese Zodiac Sign is : Snake (蛇 / Shé)")
    elif bbbyear==7:
        print("\nYour Chinese Zodiac Sign is : Horse (马 / Mǎ)")
    elif bbbyear==8:
        print("\nYour Chinese Zodiac Sign is : Goat (羊 / Yáng)")
    elif bbbyear==9:
        print("\nYour Chinese Zodiac Sign is : Monkey (猴 / Hóu)")
    elif bbbyear==10:
        print("\nYour Chinese Zodiac Sign is : Rooster (鸡 / Jī)")
    elif bbbyear==11:
        print("\nYour Chinese Zodiac Sign is : Dog (狗 / Gǒu)")
    elif bbbyear==12:
        print("\nYour Chinese Zodiac Sign is : Pig (猪 / Zhū)")
else:
    print("\nInvalid Year, it should not be earlier than 1900.")
