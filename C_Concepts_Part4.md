Part 4

# **Global Variable, Stack, Heap. -- Your Variables' Lifetime and Scope**

One thing beginners usually unaware of is the life-cycle of variables. Because C support pointers, something a pointer points to may not be always alive, it may be deallocated at some point of time. Basically there are 3 places for storing data in a program: the data segment, the stack and the heap. Global variables is allocated at the start of the program in the data segment and it is always alive during the life of the program. Local variable declared in functions (not with a &#39;<code>static</code>&#39; key word) are allocated at the start of the function call and deallocated when the function return. It is allocated in the stack. If pointers to them are stored in global variables they will point to something no longer exist after the function returns.

If the local variable in a function is declared with the &#39;<code>static</code>&#39; keyword then it will be allocated in the data section like global variable and have the same life time but then not each function call will create its own copy of the variable but all of them refer to one single copy of the variable. Therefore the function is said to have side-effect which is something have to be aware of when this function is called from multi-threads or this function is a recursive function.

If you call <code>malloc(s)</code> and <code>s = 0</code>, it may return you <code>NULL</code> or non <code>NULL</code> depends on implementation, so it should be prevented because if it return <code>NULL</code>, then your logic may think that it is out of memory and do something that is not supposed to be done.

# **There Is No Pass By Reference In C. It Is Always Pass By Value**

You can say passing array is an exception. But a better way to think of it is: Let&#39;s assume pass by value is always true (no exception), then we can view that parameter passing as a form of value assignment: The caller assign values to the local variables (the arguments) of the calling function at the monment it calls a function. When it comes to array,  it happens to follow the rvalue/lvalue counter-intuitive behaviors described in Part 3. And also function cannot return array in C. If we view it as a form of value assignment too, then it also happens to follow the rule of rvalue/lvalue rule for array. By taking this point of view, we can minimize the no. of exceptions in the grammer of the language. That is good for our brain because there are less things needed to remember. Just like if you use the Sun as the origin of the coordinate axis rather then the Earth, the equations to describe the movement of other solar system planets will be much simpler. 

Following this way of thinking we can say we are only emulating &#39;Pass By Reference&#39; by ourself by explicitly passing a pointer to a function.

When a function has argument which is a pointer to object (e.g. <code>struct s\*</code>, <code>char a[]</code>) , it should be clearly state in comment and document that this is intended for input, output or both. A better way is add a const in front to indicate this is for input only and the caller don&#39;t need to worry that document and real implement not matching because this is enforced by the language.

If a function has to return data of unkonwn variable size, one way is to let the function using <code>malloc()</code> to allocat the storage for it. Then the comment and document have to clearly state that it is the caller&#39;s responsibility to free it after use. This can either be done by return the pointer in the function return value or by a pointer to pointer argument. In the later case, if it is also used for input, let&#39;s say the argument is: <code>obj \*\*ppo</code>, and the input <code>\*\*ppo</code> is allocated by malloc, then the caller has to make sure it has keep a copy of <code>\*ppo</code> because <code>\*ppo</code> will be overwritten by the calling function. Similar to &#39;pointer to pointer&#39; is &#39;pointer to struct with pointer field&#39;. This is more subtle and beginner usually forget about it. For example:
<pre>
void f(int **ppi)
{
   printf(&quot;intput is:%d\n&quot;, **ppi);
   *ppi = (int*)malloc(10 * sizeof(int)); //over writing *ppi
    //... write something to **ppi
 }

// Wrong Implementation
int main()
{
   int *pi;

   pi = (int*)malloc(1*sizeof(int));
   *pi = 2;
   f(&amp;pi);
   //.. read *pi and do something according to the value
   free(pi); // this is not freeing the memory from the malloc() call few lines above. The pointer value is over written!! Memory leak. 

   return 0;
}

// Correct Implementation
int main()
{
   int *pi;
   int *pi_copy;  // to keep a copy of pi as its value will be over written by f();

   pi = (int*)malloc(1*sizeof(int));
   pi_copy = pi;
   *pi = 2;
   f(&amp;pi);
   free(pi_copy);  // freeing the memory from the malloc() call few lines above. 
   // .. read *pi and do something according to the value
   free(pi); // freeing the memory malloc() by f()

   return 0;
}
</pre>
For pointer to struct with pointer field:
<pre>
struct s{
  int *pi;
};

void f(struct s *ps)
{
   printf(&quot;intput is:%d\n&quot;, *(ps-&gt;pi));
   ps-&gt;pi = (int*)malloc(10 * sizeof(int)); //over writing ps-&gt;pi
    //... write something to *(ps-&gt;pi)
}

// Wrong Implementation
int main()
{
   struct s s;

   s.pi = (int*)malloc(1*sizeof(int));
   s.pi = 2;
   f(&amp;s);
   //.. read *(s.pi) and do something according to the value
   free(s.pi); // this is not freeing the memory from the malloc() call few lines above. The pointer value is over written!! Memory leak.

   return 0;
}

// Correct Implementation
int main()
{
   struct s s;
   int *s_pi_copy;  // to keep a copy of s.pi as its value will be over written by f();

   s.pi = (int*)malloc(1*sizeof(int));
   s_pi_copy = s.pi;
   *(s.pi) = 2;
   f(&amp;s);
   free(s_pi_copy);  // freeing the memory from the malloc() call few lines above.
   // .. read *(s.pi) and do something according to the value
   free(s.pi); // freeing the memory malloc() by f()

   return 0;
}
</pre>
# **Comparison operators following the rule of expression evaluation, different from the way it is used in mathematics**

If you want to check whether x is between 2 or 7 exclusive, a beginner may write:
<pre>
if (2&lt;x&lt;7) // wrong. Even x is &gt;= 7, the condition will also evaluated as true
{
   ...
}
</pre>
which will not work as he/she expects. The correct way should be:
<pre>
if (2&lt;x &amp;&amp; x&lt;7)
{
   ...
}
</pre>
This is because people usually start learning mathematics more earlier then start learning programming. As some of the mathematics syntax is same as C syntax, therefore they think this one is also true.

# **Be Aware of Endianness and Struct Field Alignment**

If you know what Endianness and Struct Field Alignament are, then you probabily will be aware of them. If you don't know such things exist, then of cause you won't. Code that simply convert multi-byte integers or structs between byte stream by using type casting will make it not portable.

For example, in network programming, as fields in IP packet header is Big Endian, you should not assume the socket program you write only compiled for Big Endian machine. Therefore the following macros are defined to change/keep the endianness depend on the compiler.
<pre>
uint32_t htonl(uint32_t hostlong);
uint16_t htons(uint16_t hostshort);
uint32_t ntohl(uint32_t netlong);
uint16_t ntohs(uint16_t netshort);
</pre>

The byte offset of fields (alignment) and so that size of a struct depends on compiler. gcc has compiler directive to change it.
<pre>
#include <stdio.h>
void main(void)
{
	struct {
		char c;
		int i;
	}s;

	struct {
		char c;
		int i;
	}__attribute__((packed)) s_pack;
	
	printf("sizeof(s) = %d\nsizeof(s_pack) = %d\n", sizeof(s), sizeof(s_pack));
}
</pre>
output:
<pre>
sizeof(s) = 8
sizeof(s_pack) = 5
</pre>
Some compilers have compiler switch to change it rather then explicitly specifing in .c file. This may cause error if struct content is dumped out to file and read by other program with wrong assumption on struct alignment. If you don't have reason like size or speed or whatever to use binary format then plain text format like XML or JSON may be good for storing or transfering data as there is no need to worry about endian and struct alignment.

Also some CPU may require 4-byte integer to be stored beginning at 4-byte boundary. For example at address <code>0xf1348074</code> but not at <code>0xf1348071</code> (must be divisible by 4). So type casting a pointer to any byte in a <code>char[]</code> array to a <code>int*</code> pointer may cause error.  

[Part 1](https://github.com/winkeung/C-Concepts/blob/master/C_Concepts_Part1.md)

[Up](https://github.com/winkeung/C-Concepts/blob/master/README.md)
