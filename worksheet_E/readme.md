(a) 
~~~~
S2 = 0 
S3 = S0

while s3 != 0:
      S3 -= 1
      S2+= S1
~~~~

(b)
S3 = S0 but S3 also equals 0 so it will go through the loop and add S1 to S2 until S3 = 0 and by decresing S3 by 1 every time it loops, so it ends up adding S1 to S2 S0 amount of times.

(c)
~~~
s0 = 10
s1 = 1

while s0 != 0:
    s2 = 0
    s3 = s0
    while s3 != 0:
        s2 += s1
        s3 -= 1
    s1 = s2
    s0 -= 1
~~~

(d)
because the inner loop keeps looping until it has looped 1 less time than the outer loop. In the inner loop the value of s1 is multiplied by the number of loops and gets stored in s2 until the inner loop is finished and this is when s1 = s2 for when the inner loop starts its next loop, so if you put in 10 in the end you would get (10x9) the first loop, (10x9x8) the second and eventually you would end up with(10x9x8x7x6x5x4x3x2x1) when it is finished.

(e)
~~~
addi $s0, $zero, 10
addi $s1, $zero, 1

loop:
mult $s1, $s0
mflo $s2
addi $s0, $s0, -1
addi $s1, $s2, 0
bne $s0, $zero, loop
~~~
