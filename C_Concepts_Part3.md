
Part 3

# **The Confusing Duality Between Arrays and Pointers**

This is the second counter-intuitive features of C that confuses a lot of beginners (The first is the &#39;declare reflect use&#39; declaration style). For integer variables in C, you can do the following:
<pre>
int i = 2;
int j;

j = i;
</pre>
but for array variables:
<pre>
int a[2] = {1,2};
int b[2];

b = a; // illegal
</pre>
When array variable name appear in normal C statement, it will be evaluated to a pointer to its 1st element. Another counter-intuitive thing is index operator can operate on pointer. But actually they are 2 different concepts:
<pre>
int a[2];
int *pi = &amp;a[0]; 
int *pi = a; // same as the line above, by utilizing a just mentioned counter-intuitive feature of C

a[1] = 1;
pi[1] = 1;  //same effect as above
</pre>
A guess may be this is to make pointer and array inter-changeable for easy refactoring. Following is a table showing when array and pointer behave the same and when not the same in different situations:

<table style="width: 665px;" cellspacing="0" cellpadding="4" border="1">
 <colgroup><col width="143">
 <col width="175">
 <col width="175">
 <col width="137">
 </colgroup><tbody>
<tr valign="TOP">
  <td rowspan="2" width="143"><div align="CENTER">
<b>Situations</b></div>
</td>
  <td colspan="2" width="359"><div style="margin-bottom: 0.2in;">
<b>T a[n];</b></div>
<b>T *p = &amp;a[0];  </b>
   </td>
  <td rowspan="2" width="137"><div align="CENTER">
<b>Comment</b></div>
</td>
 </tr>
<tr valign="TOP">
  <td width="175"><b>Array 'a'</b></td>
  <td width="175"><b>Pointer 'p'</b></td>
 </tr>
<tr valign="TOP">
  <td width="143"><span style="background: #ffff00;">Assigned by (i.e.lvalue)</span></td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b><span style="background: #ffff00;">a
   = &lt;expression&gt;;</span></b></div>
<span style="background: #ffff00;">Illegal and
   counter-intuitive.</span></td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b><span style="background: #ffff00;">p
   = &lt;expression&gt;;</span></b></div>
<span style="background: #ffff00;">OK.</span></td>
  <td width="137"><span style="background: #ffff00;">Because '<b>a</b>' is
   evaluated as '<b>&amp;a[0]</b>', a constant pointer value.</span></td>
 </tr>
<tr valign="TOP">
  <td width="143">Assigned to (i.e. rvalue)</td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b>b = a;</b></div>
OK. But counter-intuitive. 'a' will be evaluated to '&amp;a[0]'.
   So 'b' has to be 'T*', not 'T[n]'.</td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b>q = p;</b></div>
OK.</td>
  <td width="137">Array behaves like Pointer. 
   </td>
 </tr>
<tr valign="TOP">
  <td width="143">Array operator</td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b>b = a[1];</b></div>
<div style="margin-bottom: 0.2in;">
<b>a[1] = c;</b></div>
OK. 
   </td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b>q = p[1];</b></div>
<div style="margin-bottom: 0.2in;">
<b>p[1] = r;</b></div>
<div style="margin-bottom: 0.2in;">
OK but counter-intuitive.</div>
q is of type 'T'.</td>
  <td width="137">Pointer behaves like Array. 
   </td>
 </tr>
<tr valign="TOP">
  <td width="143">Dereference operator</td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b>*a</b></div>
OK but counter-intuitive. Equivalent to <b>a[0]</b>.</td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b>*p</b></div>
OK.</td>
  <td width="137">Array behaves like Pointer. 
   </td>
 </tr>
<tr valign="TOP">
  <td width="143"><span style="background: #ffff00;">Address of operator</span></td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b><span style="background: #ffff00;">&amp;a</span></b></div>
<span style="background: #ffff00;">OK. Of type 'T (*)[n]'.</span></td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b><span style="background: #ffff00;">&amp;p</span></b></div>
<span style="background: #ffff00;">OK. Of type 'T **'</span></td>
  <td width="137"><span style="background: #ffff00;">Behave differently. It is
   intuitive.</span></td>
 </tr>
<tr valign="TOP">
  <td width="143">As Function Argument 
   </td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b>f(T a[n]);</b></div>
OK but counter-intuitive. Equivalent to T *a. This means there
   will be no space revered for a array in function's local scope but
   instead just a pointer pointing to the address the caller passed
   in. Therefore the <b>n</b> in the index operator has no effect and
   can be omitted. One use is to&nbsp; tell programmers the array
   size expected by this function but it is not enforced by the
   language.</td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b>f(T *p);</b></div>
OK.</td>
  <td width="137">Array behaves like pointer.</td>
 </tr>
<tr valign="TOP">
  <td width="143">Pass to Function</td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b>f(a);</b></div>
OK but counter-intuitive. 'f' will not get a local copy of '<b>a</b>'
   but a pointer to the first element of '<b>a</b>' (<b>&amp;a[0]</b>).</td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b>f(p);</b></div>
OK</td>
  <td width="137">Array behaves like pointer.</td>
 </tr>
<tr valign="TOP">
  <td width="143"><span style="background: #ffff00;">'sizeof()' operator</span></td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b><span style="background: #ffff00;">sizeof(a)</span></b></div>
<span style="background: #ffff00;">OK. Return n*sizeof(T)</span></td>
  <td width="175"><div style="margin-bottom: 0.2in;">
<b><span style="background: #ffff00;">sizeof(p)</span></b></div>
<span style="background: #ffff00;">OK.</span></td>
  <td width="137"><span style="background: #ffff00;">Behave differently. It is
   intuitive.</span></td>
 </tr>
</tbody></table>

That means, in a C program you can change array to pointer or pointer to array by just change the lines of code including the declaration and also the lines using the operators in yellow background in the table above. For example:
<pre>
void f(int a[]);

int main()
{
  int a[2];

  a[0] = 1;
  a[1] = 2;
  f(a);

  printf(&quot;The size of a:%d&quot;, sizeof(a));
  return 0;
}
</pre>
change the code to use pointer instead of array:
<pre>
void f(int a[]);

int main()
{
  int *a; //&lt;--- chagne
  a = (int*)malloc(2*sizeof(int)); //&lt;--- change

 a[0] = 1; // &lt;----no change
 a[1] = 2; // &lt;--- no change
 f(a); //&lt;-- no change

  printf(&quot;The size of a:%d&quot;, 2*sizeof(int)); //&lt;--- chanage
  return 0;
}
</pre>
# **Pointer Arithmetic:**

Integer addition and subtraction can be applied to pointer type, but the no. you add/subtract means the no. of objects the pointer have to skip forwards or backwards. For example
<pre>
int a[10];
int *p=a;

p = p+3; //means the address is increased by 3*4 = 12 bytes because integer is 4-byte long.
</pre>
# **Nested Arrays on Function Argument List:**

For example:

<code>void f(int a[2][3][4]);</code>

is equivalent to:

<code>void f(int a[][3][4]);</code>

is equivalent to:

<code>void f(int (\*a)[3][4]);</code>

# **C String:**

String is not a built-in data type of C although C supports string literal. e.g. &quot;hello&quot;. It is a convention used by the strxxx() functions in C standard library to represent string as a char array with &#39;<code>/0</code>&#39; as the terminating character. As string is an array, it is subjected to the counter-intuitive behavior of C mentioned above. And other thing that beginners usually get trapped is that they usually forget about the null character  at the end. They forget to allocate space for it. They forget to add one at the end. They forget to count it. They forget to copy it along with other characters in the string.

WARNING:
**PLEASE DON&#39;T FORGET THE NULL CHARACTER AT THE END OF A C STRING.**

[Part 4](https://github.com/winkeung/C-Concepts/blob/master/C_Concepts_Part4.md)
[Top](https://github.com/winkeung/C-Concepts/blob/master/README.md)

