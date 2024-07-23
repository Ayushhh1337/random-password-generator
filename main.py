import random;

upp_letters = "ABCDEFGHIJKLMNOPQRST";
low_letters = upp_letters.lower();
digits = "0123456789";
symbols = "(){}[],;:-_/|\\?+#$%@"

upper, lower, nums , syms = True, True , True , True;

all = "";

if upper:
    all += upp_letters;
if lower:
    all +=low_letters;
if nums:
    all += digits;
if syms:
    all+= symbols;
    
length = 10;
amount = 10;

for x in range(amount):
    password = "".join(random.sample(all,length));
    print(password);