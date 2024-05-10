#include <stdio.h>
#include <stdlib.h>

struct node
{
	int data;
	struct node *right;
	struct node *left;
};
struct node *root = NULL;

struct node *create_node(int val)
{
	struct node *temp;
	temp = malloc(sizeof(struct node));
	temp->data = val;
	temp->left = NULL;
	temp->right = NULL;
	return temp;
}

struct node *insert(struct node *ptr, int val)
{
	if (ptr == NULL) // tree mt
	{
		return create_node(val);
	}

	if (val < ptr->data)
	{
		ptr->left = insert(ptr->left, val);
	}
	else
	{
		ptr->right = insert(ptr->right, val);
	}
	return ptr;
}
struct node *delete(struct node *ptr, int val)
{
	if (ptr == NULL)
	{
		return root;
	}
	// traverse to node
	// if (val < ptr->data)
}

void inorder(struct node *root)
{
	if (root != NULL)
	{
		inorder(root->left);
		printf("%d\t", root->data);
		inorder(root->right);
	}
}
void preorder(struct node *root)
{
	if (root != NULL)
	{
		printf("%d\t", root->data);
		inorder(root->left);
		inorder(root->right);
	}
}
void postorder(struct node *root)
{
	if (root != NULL)
	{
		inorder(root->left);
		inorder(root->right);
		printf("%d\t", root->data);
	}
}
int main()
{
	int num, op;
	do
	{

		printf("\n1 Insert element");
		printf("\n2 Delete element-x");
		printf("\n3 Inorder traversal");
		printf("\n4 Preorder traversal");
		printf("\n5 Postorder traversal");
		printf("\n6 Exit\n");
		scanf("%d", &op);

		switch (op)
		{
		case 1:
			printf("\nEnter data:");
			scanf("%d", &num);
			root = insert(root, num);
			break;
		case 2:
			break;
		case 3:
			printf("\nInorder traversal:\n");
			inorder(root);
			break;
		case 4:
			printf("\nPreorder traversal:\n");
			preorder(root);
			break;
		case 5:
			printf("\nPostorder traversal:\n");
			postorder(root);
			break;
		}
	} while (op != 6);

	return 0;
}
