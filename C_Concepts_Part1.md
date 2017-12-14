# **C Concepts**

I found that most of the books or web sites teaching C to beginners doesn&#39;t explain the subtle part of  the concepts in C clearly enough or put enough emphasis/warning on them. Those concepts will usually trap beginners. Once you mastered all these subtle concepts then you will suddenly realize that actually C is a language with just a small number of  keywords and concepts to remember. And then you will also start to appreciate the minimalist design of C. This series of posts is not intended to be a complete tutorial of the C language but it can be used as supplementary materials to those tutorials.  Lets&#39; talk about data type first...

## **C Data Types:**

Do you know what this means?
<pre>
char **var[12][3];
</pre>
If you know the answer, then skip this section, if not, after finish reading this section, you will find it very easy to decode it.

It can be said that C only have one kind of built-indata types which are NUMBERs. User can define new data types using number types as basic building blocks according to some rules which I summarize them into three rules:

1. Grouping data together in some ways (array, structure and union).
2. Treating the memory location(the address) of data as a kind of data (pointer).
3. Applying  rule no.1 or 2 to also the new data types (arrays, structures, unions and pointers) just created.

Because of rule no.3 (which can be applied repeatedly on new data type just created), things can be made really complicated. And the counter-intuitive way C declare this things make it confusing for beginners (e.g. <code>char **var[12][3]</code> -- it will be shown how to decode things like this later)

In other words, all data type in C is of the form:

some basic built-in type(s) (+ rule(s))

In C, there are only 2 main categories of numbers (whole number and floating point number) and under these 2 categories they are sub-divided by their sizes and whether they support sign(positive/negative) or not:

### **C Basic Data Type -- Number:**

1. Whole Number
**e.g. long long, signed int, unsigned int, short...**

2. Floating Point Number ** **
**e.g. float,double**...

  **Warning: Numeric** literal constants **appeared in C statements also get data types mentioned above associated with them too. The rules that apply to variables of a certain type also apply to constants of the same type.** For example:

**long long v;**
**long long v1;**

**v = 0xfffffffe + 2ll; // the constant 2 is of &#39;long long&#39; type**
**v1= 0xfffffffe + 2;**
**printf(&quot;%lld %lld\n&quot;, v, v1);**

program output:

4294967296 0

**if (1/2&gt;0) **
**  printf(&quot;yes\n&quot;);**
**else**
**  printf(&quot;no\n&quot;);**

**if (1.0/2&gt;0)**
**  printf(&quot;yes&quot;\n);**
**else**
**  printf(&quot;no\n&quot;);**

program output:
no
yes

### **There are ONLY 1-D Arrays in C. That are no Multi-Dimensional Arrays in C but Nested 1-D Arrays:**

If you know how to analyze the syntax of an multi-dimensional array&#39;s declaration,  you will agree that it is more appropriate to call it an &#39;nested array&#39; rather then &#39;multi-dimensional array&#39;. An &#39;nested array&#39; is an array whose elements are also arrays. An array of array(s) (of array(s)...) of something. The word &#39;something&#39; here can be basic data type, structure, union or pointer. **In C, there is only 1-D array.** If you have a array of struct, you can add for example &#39; **.field**&#39; after the array index operator like: &#39;**as[1].field**&#39; to access the field. Similarly, if you have an array of arrays, you access the inner array&#39;s element by attaching one more &#39;**[]**&#39; to access it: e.g. **aa[1][2]**, just like you add a &#39; **.field**&#39; in the case of **struct**. &#39;**as[1]&#39;** returns you the struct at index 1, **&#39;aa[1]**&#39; returns you the array at index 1.You add **&#39;.field&#39;** or &#39;**[]**&#39; to further access its internal objects.

For example,
Converting **int a[4]** into English: **a** is an 4-element array (of integers).
Converting **int a2d[3][4]** into English: **a2d** is an 3-element array (of 4-element arrays (of integers)).
Converting **int a3d[2][3][4]** into English: **a3d** is an 2-element array (of 3-element arrays (of 4-element arrays (of integers))).

or:
Converting **int a[4]** into English: **a** is an array (of 4 integers).
Converting **int a2d[3][4]** into English: **a2d** is an array (of 3 arrays (of 4 integers)).
Converting **int a3d[2][3][4]** into English: **a3d** is an array (of 2 arrays (of 3 arrays (of 4 integers))).

or
..
Converting **int a3d[2][3][4]** into English: 4 integers get together to form an array and 3 instances of this array get together to form an nested array and 2 instances of this nested array get together to form a multi-layer nested array and lets&#39; call it **a3d**.

(This web site can convert your C declaration into English [http://www.lemoda.net/c/cdecl/index.cgi?text=explain+int+a[3]%3B](http://www.lemoda.net/c/cdecl/index.cgi?text=explain+int+a%5b3%5d%3B))

Visualizing **a3d[2][3][4]**:

 ![](data:image/*;base64,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)
 [ ](https://3.bp.blogspot.com/-6xoqGiGJh7g/UPf8dvb1s8I/AAAAAAAAABM/8vXaXpGSgZ8/s1600/array_2x3x4.jpg)

 or

 ![](data:image/*;base64,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)

The memory layout for the 3-D array **a3d** will look like this, the integer on the top will be located at low memory address:

| _a3d_ | _a3d[0]_ | _a3d[0][0]_ | _a3d[0][0][0]_ | **int** |
| --- | --- | --- | --- | --- |
| _a3d[0][0][1]_ | **int** |
| _a3d[0][0][2]_ | **int** |
| _a3d[0][0][3]_ | **int** |
| _a3d[0][1]_ | _a3d[0][1][0]_ | **int** |
| _a3d[0][1][1]_ | **int** |
| _a3d[0][1][2]_ | **int** |
| _a3d[0][1][3]_ | **int** |
| _a3d[0][2]_ | _a3d[0][2][0]_ | **int** |
| _a3d[0][2][1]_ | **int** |
| _a3d[0][2][2]_ | **int** |
| _a3d[0][2][3]_ | **int** |
| _a3d[1]_ | _a3d[1][0]_ | _a3d[1][0][0]_ | **int** |
| _a3d[1][0][1]_ | **int** |
| _a3d[1][0][2]_ | **int** |
| _a3d[1][0][3]_ | **int** |
| _a3d[1][1]_ | _a3d[1][1][0]_ | **int** |
| _a3d[1][1][1]_ | **int** |
| _a3d[1][1][2]_ | **int** |
| _a3d[1][1][3]_ | **int** |
| _a3d[1][2]_ | _a3d[1][2][0]_ | **int** |
| _a3d[1][2][1]_ | **int** |
| _a3d[1][2][2]_ | **int** |
| _a3d[1][2][3]_ | **int** |

Total 2x3x4 = 24 integers.

In the declaration of a nested array,  the no. in the square bracket nearest to the variable identifier is the top level array&#39;s length.

An nested array&#39;s element is accessed like this in a C statement:

**i = a[0][1][3]; **

But actually **a** is an array of arrays of arrays, the expression can be equivalently re-written as:

**i = ((a[0])[1])[3];**

This emphasizes how the expression is evaluated form top level array downwards to the bottom level array. This reveals the fact that **a** is actually an array of arrays of arrays behind the scene. In this expression the sub expression **a[0]** and **a[0][1]** can also appear by themselves alone in C statement **,** like:


**some\_variable1 = a[0];**
**some\_variable2 = a[0][1];**

**In C, the syntax for (nested) array declaration make use of the syntax for accessing (nested) array element  in normal C statement**.For example, to analyze **int a[2][3][4]**, first re-write it as **int ((a[2])[3])[4]** to emphasize the order of evaluation.  And then, the expression **int ((a[2])[3])[4] **can be analyzed starting from the inner most bracket like this:

1. **a[****2****]**: the **&#39;[2]&#39;** array index operator operating on **a** means object **a** is an array of **2** objects, the expression  **(a[2])** is evaluated as one such object.
2. **(a[2])[****3****]**: object **(a[2])** is an array of **3** objects **,** the expression  **((a[2])[3])** is evaluated as one such object.
3. **((a[2])[3])[****4****]:** object **((a[2])[3])** is an array of **4** objects, the expression **((a[2])[3])[4]** is evaluated as one such object.
4. **int ((a[2])[3])[4]:** object **((a[2])[3])[4]** is an integer.

By substituting no.4 into no.3, we get:
1....
2...
3. **((a[2])[3])[****4****]:** object **((a[2])[3])** is an array of **4** object integers **.**

By substituting no.3 into no.2, we get:
1...
2.**(a[2])[****3****]**: object **(a[2])** is an array of **3** objectarrays of 4 integers_._

And finally we reduce it into:
1. **a[****2****]**: object **a** is an array of **2** object arrays of 3 arrays of 4 integers_._
** **
Which explains why the no. in the square bracket nearest to the variable identifier is the top level array&#39;s length.

It may seem that it is not necessary to apply this kind of lengthy analysis to understand nested array declaration but when it mixed with pointer operators, then it is very useful.

The declaration statement is like a demo showing you how a known type of object is extracted out from a variable of unknown type in order to let you know what type the variable is (how that type is constructed from the known type). This is commonly called &#39;declaration reflects use&#39;. For example: ** **

**int a[2][3][4]**;

Which is like saying that:

If the &#39;get element operator -- **[]**&#39; is applied 3 times successively (**a[][][]**) on &#39; **a**&#39;, then we will get a **int** object.

In this example the variable of unknown type is **a** and the know type of object is **int**.

It let you know how something is constructed by showing you the procedure of disassembling it.

a3d can also be declared like this:

**typedef int       A4[4];**
**typedef A4      A3x4[3];**
**typedef A3x4  A2x3x4[2];**

**A2x3x4 a3d;**

It starts from the inner most array to the outer most array, opposite to this style**: int a3d[2][3][4]**. And it is the later style that make it difficult for beginner (especially when mixed with pointer operators). It is because it starts from describing the final composite type(in this case the outer most array -- an 2-element array of something yet to be defined) and then successively decomposes it down to the built-in basic type(in this case **int** ) in a single expression. A good understanding of expression evaluation is needed.

Of cause you can use this &#39;array of arrays of ...&#39; thing to represent 2-D or n-D matrix (they are truly multi-dimensional array conceptually). Just remember that for example in a 2-D matrix, extracting a row from it is very different from extracting a column from it. One is easier or harder then the other depends on whether you define a row as the top level array element or column as the top level array element. For example:

**int matrix\_2d[2][3];** //a 2-D matrix of 2 rows(indexes: 0,1), 3 columns(indexes 0,1,2) --- row as the top level array element

// to extract the whole row of index no.1
**some\_variable1 = matrix\_2d[1];**

// to extract the whole column of index no.2
**some\_variable2 = matrix\_2d[][2]; //** no such syntax in C, have to extract element by element with a for loop or something similar.

That is why nested array is a better name then multi-dimensional array. Because the word mutli-dimensional usually implies that all dimensions have the same status, meaning if an operation can be applied on one dimension then it can also be applied on any of the other dimensions.

The initialization for nested array is like this:

int a3d[2][3][4]=
{
  {
      {1,2,3,4},         //a3d[0][0]
      {5,6,7,8},         //a3d[0][1]
      {9,10,11,12}    //a3d[0][2]
   },  //a3d[0]
   {
     {13,14,15,16},  //a3d[1][0]
     {17,18,19,20},  //a3d[1][1]
     {21,22,23,24}   //a3d[1][2]
   } //a3d[1]
}; //a3d

which reflects the nested nature of it.


(to be continue...)

