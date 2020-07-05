Part 3

# **The Confusing Duality Between Arrays and Pointers**
# **(Array is second class citizen in C. Pointer steal its operator []. It has to disguise as Pointer in order to use this operator)**

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
However, this is legal:
<pre>
struct s{
	int i[2];
};
struct s a = {{1,2}};
struct s b;

b = a; // legal
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

<table cellspacing="0" cellpadding="4" border="1">
 <colgroup><col>
 <col>
 <col>
 <col>
 </colgroup><tbody>
<tr valign="TOP">
  <td rowspan="2" ><div align="CENTER">
<b>Situations</b></div>
</td>
  <td colspan="2" ><div style="margin-bottom: 0.2in;">
<code>T a[n];</code></div>
<code>T *p = &amp;a[0];</code>
   </td>
  <td rowspan="2" ><div align="CENTER">
<b>Comment</b></div>
</td>
 </tr>
<tr valign="TOP">
 <td ><b>Array '<code>a</code>'</b></td>
 <td ><b>Pointer '<code>p</code>'</b></td>
 </tr>
<tr valign="TOP">
  <td ><span style="background: #ffff00;">1. Assigned by (i.e.lvalue)</span></td>
  <td ><div style="margin-bottom: 0.2in;">
<code><span style="background: #ffff00;">a
   = &lt;expression&gt;;</span></code></div>
<span style="background: #ffff00;">Illegal and
   counter-intuitive.</span></td>
  <td ><div style="margin-bottom: 0.2in;">
<code><span style="background: #ffff00;">p
   = &lt;expression&gt;;</span></code></div>
<span style="background: #ffff00;">OK.</span></td>
  <td ><span style="background: #ffff00;">Because '<code>a</code>' is
   evaluated as '<code>&amp;a[0]</code>', a constant pointer value.</span></td>
 </tr>
<tr valign="TOP">
  <td >2. Assigned to (i.e. rvalue)</td>
  <td ><div style="margin-bottom: 0.2in;">
<code>b = a;</code></div>
OK. But counter-intuitive. '<code>a</code>' will be evaluated to '<code>&amp;a[0]</code>'.
   So '<code>b</code>' has to be '<code>T*</code>', not '<code>T[n]</code>'.</td>
  <td ><div style="margin-bottom: 0.2in;">
<code>q = p;</code></div>
OK.</td>
  <td >Array behaves like Pointer. 
   </td>
 </tr>
<tr valign="TOP">
  <td >3. Array operator</td>
  <td ><div style="margin-bottom: 0.2in;">
<code>b = a[1];</code></div>
<div style="margin-bottom: 0.2in;">
<code>a[1] = c;</code></div>
OK. 
   </td>
  <td ><div style="margin-bottom: 0.2in;">
<code>q = p[1];</code></div>
<div style="margin-bottom: 0.2in;">
<code>p[1] = r;</code></div>
<div style="margin-bottom: 0.2in;">
OK but counter-intuitive.</div>
<code>q</code> is of type '<code>T</code>'.</td>
  <td >Pointer behaves like Array. 
   </td>
 </tr>
<tr valign="TOP">
  <td >4. Dereference operator</td>
  <td ><div style="margin-bottom: 0.2in;">
<code>*a</code></div>
OK but counter-intuitive. Equivalent to <code>a[0]</code>.</td>
  <td ><div style="margin-bottom: 0.2in;">
<code>*p</code></div>
OK.</td>
  <td >Array behaves like Pointer. 
   </td>
 </tr>
<tr valign="TOP">
  <td ><span style="background: #ffff00;">5. Address of operator</span></td>
  <td ><div style="margin-bottom: 0.2in;">
<code><span style="background: #ffff00;">&amp;a</span></code></div>
<span style="background: #ffff00;">OK. Of type '<code>T (*)[n]</code>'.</span></td>
  <td ><div style="margin-bottom: 0.2in;">
<code><span style="background: #ffff00;">&amp;p</span></code></div>
<span style="background: #ffff00;">OK. Of type '<code>T **</code>'</span></td>
  <td ><span style="background: #ffff00;">Behave differently. It is
   intuitive.</span></td>
 </tr>
<tr valign="TOP">
  <td >6. As Function Argument 
   </td>
  <td ><div style="margin-bottom: 0.2in;">
<code>f(T a[n]);</code></div>
OK but counter-intuitive. Equivalent to <code>T *a</code>. This means there
   will be no space revered for a array in function's local scope but
   instead just a pointer pointing to the address the caller passed
   in. Therefore the <code>n</code> in the index operator has no effect and
   can be omitted. One use is to&nbsp; tell programmers the array
   size expected by this function but it is not enforced by the
   language.</td>
  <td ><div style="margin-bottom: 0.2in;">
<code>f(T *p);</code></div>
OK.</td>
  <td >Array behaves like pointer.</td>
 </tr>
<tr valign="TOP">
  <td >7. Pass to Function</td>
  <td ><div style="margin-bottom: 0.2in;">
<code>f(a);</code></div>
OK but counter-intuitive. 'f' will not get a local copy of '<code>a</code>'
   but a pointer to the first element of '<code>a</code>' (<code>&amp;a[0]</code>).</td>
  <td ><div style="margin-bottom: 0.2in;">
<code>f(p);</code></div>
OK</td>
  <td >Array behaves like pointer.</td>
 </tr>
<tr valign="TOP">
  <td ><span style="background: #ffff00;">8. 'sizeof()' operator</span></td>
  <td ><div style="margin-bottom: 0.2in;">
<code><span style="background: #ffff00;">sizeof(a)</span></code></div>
<span style="background: #ffff00;">OK. Return <code>n*sizeof(T)</code></span></td>
  <td ><div style="margin-bottom: 0.2in;">
<code><span style="background: #ffff00;">sizeof(p)</span></code></div>
<span style="background: #ffff00;">OK.</span></td>
  <td ><span style="background: #ffff00;">Behave differently. It is
   intuitive.</span></td>
 </tr>
</tbody></table>

That means, in a C program you can change array to pointer or pointer to array by just change the lines of code including the declaration and also the lines using the operators in 1, 5, 8 in the table above. For example:
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
  int *a; //&lt;--- change
  a = (int*)malloc(2*sizeof(int)); //&lt;--- change

 a[0] = 1; // &lt;----no change
 a[1] = 2; // &lt;--- no change
 f(a); //&lt;-- no change

  printf(&quot;The size of a:%d&quot;, 2*sizeof(int)); //&lt;--- change
  return 0;
}
</pre>
# **Pointer Arithmetic: 1 + 1 is not always equal to 2**

Integer addition and subtraction can be applied to pointer type, but the no. you add/subtract means the no. of objects the pointer have to skip forwards or backwards. For example
<pre>
int *p=(int*)1;
printf("%p %p\n", p, p+1); // 0x1, 0x5 because int is 4 byte long
</pre>
# **Array/Nested Array on Function Argument List: You Do Not Get What You Write**

Here nested array is just a special case of array, it doesn't matter the element of the array is also array or other kinds of object.

For example:

<code>void f(int a[10]);</code>

is equivalent to :

<code>void f(int \*a);</code>

is also equivalent to :

<code>void f(int a[]);</code>

Another example:

<code>void f(int a[2][3][4]);</code>

is equivalent to:

<code>void f(int a[][3][4]);</code>

is also equivalent to:

<code>void f(int (\*a)[3][4]);</code>

Therefore it is get converted to pointer to the type of the array element.

# **C String: No Such Data Type in C**

String is not a built-in data type of C although C supports string literal. e.g. <code>&quot;hello&quot;</code>. It is a convention used by the <code>strxxx()</code> functions in C standard library to represent string as a char array with &#39;<code>/0</code>&#39; as the terminating character. As string is an array, it is subjected to the counter-intuitive behavior of C mentioned above. And other thing that beginners usually get trapped is that they usually forget about the null character  at the end. They forget to allocate space for it. They forget to add one at the end. They forget to count it. They forget to copy it along with other characters in the string.

WARNING:
**PLEASE DON&#39;T FORGET THE NULL CHARACTER AT THE END OF A C STRING.**

[Part 4](C_Concepts_Part4.md)

[Up](README.md)
