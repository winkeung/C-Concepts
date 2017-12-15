
### [**C Concepts: Part 3**](https://ctatsujin.blogspot.hk/2013/01/c-concepts-part-3.html)

## **In Some Situations Arrays Behave Like Pointers and In Some Others Pointers Behave Like Arrays:**

This is the second counter-intuitive features of C that confuses a lot of beginners (The first is the &#39;declare reflect use&#39; declaration style). For integer variables in C, you can do the following:

**int i = 2;**
**int j;**

**j = i;**

but for array variables:

**int a[2] = {1,2};**
**int b[2];**

**b = a; // illegal**

When array variable name appear in normal C statement, it will be evaluated to a pointer to its1st element. Another counter-intuitive thing is index operator can operate on pointer. But actually they are 2 different concepts:

**int a[2]**
**int \*pi = &amp;a[0]; //  can be re-written by replacing &#39;&amp;a[0]&#39; with just &#39;a&#39; , utilizing a just mentioned counter-intuitive feature of C**

**a[1] = 1;**
**pi[1] = 1;  //same effect as above**

A guess may be this is to make pointer and array inter-changeable for easy refactoring. Following is a table showing when array and pointer behave the same and when not the same in different situations:

| **Situations** | **T a[n];****T \*p = &amp;a[0]; **|** Comment** |
| --- | --- | --- |
| **Array &#39;a&#39;** | **Pointer &#39;p&#39;** |
| Assigned by (i.e.lvalue) | **a = &lt;expression&gt;;** Illegal and counter-intuitive. | **p = &lt;expression&gt;;** OK. | Because &#39; **a**&#39; is evaluated as &#39;**&amp;a[0]**&#39;, a constant pointer value. |
| Assigned to (i.e. rvalue) | **b = a;** OK. But counter-intuitive. &#39;a&#39; will be evaluated to &#39;&amp;a[0]&#39;. So &#39;b&#39; has to be &#39;T\*&#39;, not &#39;T[n]&#39;. | **q = p;** OK. | Array behaves like Pointer. |
| Array operator | **b = a[1];****a[1] = c; **OK. |** q = p[1];****p[1] = r;**OK but counter-intuitive.q is of type &#39;T&#39;. | Pointer behaves like Array. |
| Dereference operator | **\*a** OK but counter-intuitive. Equivalent to **a[0]**. | **\*p** OK. | Array behaves like Pointer. |
| Address of operator | **&amp;a** OK. Of type &#39;T (\*)[n]&#39;. | **&amp;p** OK. Of type &#39;T \*\*&#39; | Behave differently. It is intuitive. |
| As Function Argument | **f(T a[n]);**OK but counter-intuitive. Equivalent to T \*a. This means there will be no space revered for a array in function&#39;s local scope but instead just a pointer pointing to the address the caller passed in. Therefore the **n** in the index operator has no effect and can be omitted. One use is to  tell programmers the array size expected by this function but it is not enforced by the language. | **f(T \*p);**OK. | Array behaves like pointer. |
| Pass to Function | **f(a);**OK but counter-intuitive. &#39;f&#39; will not get a local copy of &#39; **a**&#39; but a pointer to the first element of &#39; **a**&#39; (**&amp;a[0]**). | **f(p);**OK | Array behaves like pointer. |
| &#39;sizeof()&#39; operator | **sizeof(a)**OK. Return n\*sizeof(T) | **sizeof(p)**OK. | Behave differently. It is intuitive. |

That means, in a C program you can change array to pointer or pointer to array by just change the lines of code including the declaration and also the lines using the operators in yellow background in the table above. For example:

**void f(int a[]);**

**int main() **
**{**
**  int a[2];**

**  a[0] = 1;**
**  a[1] = 2;**
**  f(a);**

**  printf(&quot;The size of a:%d&quot;, sizeof(a));**
**  return 0;**
**}**

change the code to use pointer instead of array:

**void f(int a[]);**

**int main()**
**{**
**  int \*a; //&lt;--- chagne**
**  a = (int\*)malloc(2\*sizeof(int)); //&lt;--- change**

** a[0] = 1; // &lt;----no change**
** a[1] = 2; // &lt;--- no change**
** f(a); //&lt;-- no change**

**  printf(&quot;The size of a:%d&quot;, 2\*sizeof(int)); //&lt;--- chanage**
**  return 0;**
**}**

### **Pointer Arithmetic:**

Integer addition and subtraction can be applied to pointer type, but the no. you add/subtract means the no. of objects the pointer have to skip forwards or backwards. For example

**int a[10];**
**int \*p=a;**

**p = p+3; //means the address is increased by 3\*4 = 12 bytes because integer is 4-byte long.**

### ** **

### **Nested Arrays on Function Argument List:**

For example:
**void f(int a[2][3][4]);**

is equivalent to:

**void f(int a[][3][4]);**

is equivalent to:

**void f(int (\*a)[3][4]);**

## **C String:**

String is not a built-in data type of C although C supports string literal. e.g. &quot;hello&quot;. It is a convention used by the strxxx() functions in C standard library to represent string as a char array with &#39;/0&#39; as the terminating character. As string is an array, it is subjected to the counter-intuitive behavior of C mentioned above. And other thing that beginners usually get trapped is that they usually forget about the null character  at the end. They forget to allocate space for it. They forget to add one at the end. They forget to count it. They forget to copy it along with other characters in the string.

WARNING:
**PLEASE DON&#39;T FORGET THE NULL CHARACTER AT THE END OF A C STRING.**

[Part 3](https://github.com/winkeung/C-Concepts/blob/master/C_Concepts_Part3.md)
[Top](https://github.com/winkeung/C-Concepts/blob/master/README.md)

