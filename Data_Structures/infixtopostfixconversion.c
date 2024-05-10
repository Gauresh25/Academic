#include<stdio.h>
#include<stdlib.h>     
#include<ctype.h>
#include<string.h>
#define SIZE 15

char stack[SIZE];
int top = -1;

void push(char element)
{
	if(top >= SIZE-1)
	{
		printf("\nOVERFLOW");
	}
	else
	{
		top = top+1;
		stack[top] = element;
	}
}

char pop()
{
	char element ;

	if(top <0)
	{
		printf("stack under flow: invalid infix expression");
		exit(1);
	}
	else
	{
		element = stack[top];
		top = top-1;
		return(element);
	}
}

int operator_check(char symbol)
{
	if(symbol == '^' || symbol == '*' || symbol == '/' || symbol == '+' || symbol =='-')
	{
		return 1;
	}
	else
	{
	return 0;
	}
}

int precedence(char symbol)
{
	if(symbol == '^')
	{
		return(3);
	}
	else if(symbol == '*' || symbol == '/')
	{
		return(2);
	}
	else if(symbol == '+' || symbol == '-')
	{
		return(1);
	}
	else
	{
		return(0);
	}
}

void Infix_postfix_convert(char infix_exp[], char postfix_exp[])
{ 
	int i, j;
	char element;
	char x;

	push('(');                               
	strcat(infix_exp,")");              

	i=0;
	j=0;
	element=infix_exp[i]; 

	while(element != '\0')
	{
		if(element == '(')
		{
			push(element);
		}
		else if( isdigit(element) || isalpha(element))
		{
			postfix_exp[j] = element;              /* add operand symbol to postfix expr */
			j++;
		}
		else if(operator_check(element) == 1)        /* means symbol is operator */
		{
			x=pop();
			while(operator_check(x) == 1 && precedence(x)>= precedence(element))
			{
				postfix_exp[j] = x;                  /* so pop all higher precendence operator and */
				j++;
				x = pop();                       /* add them to postfix expresion */
			}
			push(x);
			/* because just above while loop will terminate we have
			oppped one extra element
			for which condition fails and loop terminates, so that one*/

			push(element);                 /* push current oprerator symbol onto stack */
		}
		else if(element == ')')         /* if current symbol is ')' then */
		{
			x = pop();                   /* pop and keep popping until */
			while(x != '(')                /* '(' encounterd */
			{
				postfix_exp[j] = x;
				j++;
				x = pop();
			}
		}
		else
		{ /* if current symbol is neither operand not '(' nor ')' and nor
			operator */
			printf("\nInvalid infix Expression.\n");        /* the it is illegeal  symbol */
			getchar();
			exit(1);
		}
		i++;


		element = infix_exp[i]; /* go to next symbol of infix expression */
	} /* while loop ends here */
	if(top>0)
	{
		printf("\nInvalid infix Expression.\n");        /* the it is illegeal  symbol */
		getchar();
		exit(1);
	}


	postfix_exp[j] = '\0'; /* add sentinel else puts() fucntion */
	/* will print entire postfix[] array upto SIZE */
	printf("Postfix Expression: "); 
	puts(postfix_exp);

}

/* main function begins */
int main()
{
	int i;
	char infix[SIZE], postfix[SIZE];   
	printf("\nEnter Infix expression : ");
	gets(infix);

	Infix_postfix_convert(infix,postfix);                      

	return 0;
}