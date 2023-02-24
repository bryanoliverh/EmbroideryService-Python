# EmbroideryService-Python

**This is a Python code that functions as Embroidery Service. It will firstly asks user with these options:**

```
Welcome to Bryan's Embroidery Services!
==========================================
1. Display Pricing Table
2. Request for Quote
3. Add/Update Characters' Pricings
4. Exit
```

**For Option 1:**

User will be prompted with the font size question. The font size multiplier is inside the fonts.txt file. It will multiply the value of each character with a constant multiplier based on the user-chosen font size.

```
Please enter your choice (1-4): 1
Please enter font size (24, 36, or 48): 24
Pricing for font size 24pts
===========================
A       45.00   B       79.00   C       60.00   D       56.00   E       46.00   F       50.00   G       65.00   H       45.00   I       38.00   J       49.00
K       51.00   L       36.00   M       48.00   N       55.00   O       56.00   P       53.00   Q       41.00   R       58.00   S       65.00   T       36.00
U       23.00   V       49.00   W       46.00   X       48.00   Y       54.00   Z       52.00   a       63.00   b       55.00   c       37.00   d       55.00
e       63.00   f       58.00   g       40.00   h       31.00   i       36.00   j       50.00   k       51.00   l       36.00   m       32.00   n       58.00
o       50.00   p       55.00   q       55.00   r       53.00   s       61.00   t       57.00   u       37.00   v       33.00   w       59.00   x       53.00
y       54.00   z       39.00   !       35.00   &       65.00   *       65.00   $       65.00   #       64.00   .       30.00   ,       36.00   <       38.00
>       38.00   ?       45.00   @       65.00
```

**For Option 2:**


User will be prompted to enter the characters that they want to print. If the total price > $1,  there will be a 15% discounts.

```
Welcome to Bryan's Embroidery Services!
==========================================
1. Display Pricing Table
2. Request for Quote
3. Add/Update Characters' Pricings
4. Exit
Please enter your choice (1-4): 2
Enter characters that you want to print: Bryan Oliver H
Enter font size (24/36/48): 24
Total price: $6.29

Welcome to Bryan's Embroidery Services!
==========================================
1. Display Pricing Table
2. Request for Quote
3. Add/Update Characters' Pricings
4. Exit
Please enter your choice (1-4): 2
Enter characters that you want to print: Bryan Oliver HBaEgKJKLa
Enter font size (24/36/48): 24
Total price: $11.07
Discount: $1.66
Discounted price: $9.41
```



**For Option 3:**


User will be able to add a new character into the characters.txt file.
```
Welcome to Bryan's Embroidery Services!
==========================================
1. Display Pricing Table
2. Request for Quote
3. Add/Update Characters' Pricings
4. Exit
Please enter your choice (1-4): 3   
Please enter the character to add/update pricing: /
Please enter the pricing for /: 50
The pricing for / has been updated.
Welcome to Bryan's Embroidery Services!
==========================================
1. Display Pricing Table
2. Request for Quote
3. Add/Update Characters' Pricings
4. Exit
Please enter your choice (1-4): 1
Please enter font size (24, 36, or 48): 24
Pricing for font size 24pts
===========================
A       45.00   B       79.00   C       60.00   D       56.00   E       46.00   F       50.00   G       65.00   H       45.00   I       38.00   J       49.00
K       51.00   L       36.00   M       48.00   N       55.00   O       56.00   P       53.00   Q       41.00   R       58.00   S       65.00   T       36.00
U       23.00   V       49.00   W       46.00   X       48.00   Y       54.00   Z       52.00   a       63.00   b       55.00   c       37.00   d       55.00
e       63.00   f       58.00   g       40.00   h       31.00   i       36.00   j       50.00   k       51.00   l       36.00   m       32.00   n       58.00
o       50.00   p       55.00   q       55.00   r       53.00   s       61.00   t       57.00   u       37.00   v       33.00   w       59.00   x       53.00
y       54.00   z       39.00   !       35.00   &       65.00   *       65.00   $       65.00   #       64.00   .       30.00   ,       36.00   <       38.00
>       38.00   ?       45.00   @       65.00   /       50.00
```

**For Option 4:**

User will exit the program
