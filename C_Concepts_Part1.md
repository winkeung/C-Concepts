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

## **C Basic Data Type -- Number:**

1. Whole Number
**e.g. <code>long long, signed int, unsigned int, short...</code>**

2. Floating Point Number
**e.g. <code>float,double...</code>**

  **Warning: Numeric** literal constants **appeared in C statements also get data types mentioned above associated with them too. The rules that apply to variables of a certain type also apply to constants of the same type.** For example:
<pre>
long long v;
long long v1;

v = 0xfffffffe + 2ll; // the constant 2 is of &#39;long long&#39; type
v1= 0xfffffffe + 2;
printf(&quot;%lld %lld\n&quot;, v, v1);
</pre>
program output:
<pre>
4294967296 0
</pre>
<pre>
if (1/2 &gt; 0) 
  printf(&quot;yes\n&quot;);
else
  printf(&quot;no\n&quot;);

if (1.0/2 &gt; 0)
  printf(&quot;yes&quot;\n);
else
  printf(&quot;no\n&quot;);
</pre>
program output:
<pre>
no
yes
</pre>
### **There are ONLY 1-D Arrays in C. That are no Multi-Dimensional Arrays in C but Nested 1-D Arrays:**

If you know how to analyze the syntax of an multi-dimensional array&#39;s declaration,  you will agree that it is more appropriate to call it an &#39;nested array&#39; rather then &#39;multi-dimensional array&#39;. An &#39;nested array&#39; is an array whose elements are also arrays. An array of array(s) (of array(s)...) of something. The word &#39;something&#39; here can be basic data type, structure, union or pointer. **In C, there is only 1-D array.** If you have a array of struct, you can add for example &#39; **<code>.field</code>**&#39; after the array index operator like: &#39;**<code>as[1].field</code>**&#39; to access the field. Similarly, if you have an array of arrays, you access the inner array&#39;s element by attaching one more &#39;**<code>[]</code>**&#39; to access it: e.g. **<code>aa[1][2]</code>**, just like you add a &#39; **<code>.field</code>**&#39; in the case of struct. &#39;**<code>as[1]&#39;</code>** returns you the struct at index 1, **&#39;<code>aa[1]</code>**&#39; returns you the array at index 1.You add **<code>&#39;.field</code>&#39;** or &#39;**<code>[]</code>**&#39; to further access its internal objects.

For example,
- Converting **<code>int a[4]</code>** into English: **<code>a</code>** is an 4-element array (of integers).
- Converting **<code>int a2d[3][4]</code>** into English: **<code>a2d</code>** is an 3-element array (of 4-element arrays (of integers)).
- Converting **<code>int a3d[2][3][4]</code>** into English: **<code>a3d</code>** is an 2-element array (of 3-element arrays (of 4-element arrays (of integers))).

or:
- Converting **<code>int a[4]</code>** into English: **<code>a</code>** is an array (of 4 integers).
- Converting **<code>int a2d[3][4]</code>** into English: **<code>a2d</code>** is an array (of 3 arrays (of 4 integers)).
- Converting **<code>int a3d[2][3][4]</code>** into English: **<code>a3d</code>** is an array (of 2 arrays (of 3 arrays (of 4 integers))).

or
- ...
- Converting **<code>int a3d[2][3][4]</code>** into English: 4 integers get together to form an array and 3 instances of this array get together to form an nested array and 2 instances of this nested array get together to form a multi-layer nested array and lets&#39; call it **<code>a3d</code>**.

(This web site can convert your C declaration into English [http://www.lemoda.net/c/cdecl/index.cgi?text=explain+int+a[3]%3B](http://www.lemoda.net/c/cdecl/index.cgi?text=explain+int+a%5b3%5d%3B))

Visualizing **<code>a3d[2][3][4]</code>**:

![Alt text](array_2x3x4.jpg)

 or

![Alt text](array_2x3x4_1.jpg)

The memory layout for the 3-D array **a3d** will look like this, the integer on the top will be located at low memory address:
<br>
<table style="width: 100%px;" cellspacing="0" cellpadding="4" border="1">
 <colgroup><col width="32*">
 <col width="36*">
 <col width="52*">
 <col width="65*">
 <col width="72*">
 </colgroup><tbody>
<tr>
  <td rowspan="24" width="12%"><div style="text-decoration: none;" align="CENTER">
<i>a3d</i></div>
</td>
  <td rowspan="12" width="14%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0]</i></div>
</td>
  <td rowspan="4" width="20%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0][0]</i></div>
</td>
  <td width="25%" valign="TOP"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0][0][0]</i></div>
</td>
  <td width="28%" valign="TOP"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0][0][1]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0][0][2]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0][0][3]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr>
  <td rowspan="4" width="20%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0][1]</i></div>
</td>
  <td width="25%" valign="TOP"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0][1][0]</i></div>
</td>
  <td width="28%" valign="TOP"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0][1][1]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0][1][2]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0][1][3]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr>
  <td rowspan="4" width="20%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0][2]</i></div>
</td>
  <td width="25%" valign="TOP"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0][2][0]</i></div>
</td>
  <td width="28%" valign="TOP"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0][2][1]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0][2][2]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[0][2][3]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr>
  <td rowspan="12" width="14%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1]</i></div>
</td>
  <td rowspan="4" width="20%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1][0]</i></div>
</td>
  <td width="25%" valign="TOP"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1][0][0]</i></div>
</td>
  <td width="28%" valign="TOP"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1][0][1]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1][0][2]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1][0][3]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr>
  <td rowspan="4" width="20%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1][1]</i></div>
</td>
  <td width="25%" valign="TOP"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1][1][0]</i></div>
</td>
  <td width="28%" valign="TOP"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1][1][1]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1][1][2]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1][1][3]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr>
  <td rowspan="4" width="20%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1][2]</i></div>
</td>
  <td width="25%" valign="TOP"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1][2][0]</i></div>
</td>
  <td width="28%" valign="TOP"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1][2][1]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1][2][2]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="25%"><div style="text-decoration: none;" align="CENTER">
<i>a3d[1][2][3]</i></div>
</td>
  <td width="28%"><div align="CENTER">
<b>int</b></div>
</td>
 </tr>
</tbody></table>
<br>
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

