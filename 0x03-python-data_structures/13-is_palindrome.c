#include "lists.h"

/**
 * reverse - a function that checks for a palindrome
 * in a singly linked list
 * @head: head of the node
 * Return: reversed list
 */

listint_t *reverse(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * compareLists - a function that checks for a palindrome
 * in a singly linked list
 * @head1: head of the node
 * @head2: second head
 * Return: 0 if not, 1 if it is
 */

int compareLists(listint_t *head1, listint_t *head2)
{
	while (head1 != NULL && head2 != NULL)
	{
		if (head1->n != head2->n)
		{
			return (0);
		}
		head1 = head1->next;
		head2 = head2->next;
	}
	if (head1 == NULL && head2 == NULL)
	{
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - a function that checks for a palindrome
 * in a singly linked list
 * @head: head of the node
 * Return: 0 if not, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half;
	listint_t *prev_of_slow = NULL;
	listint_t *midnode = NULL;

	int res = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_of_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			midnode = slow;
			slow = slow->next;
		}

		second_half = slow;
		prev_of_slow->next = NULL;
		second_half = reverse(second_half);
		res = compareLists(*head, second_half);

		second_half = reverse(second_half);

		if (midnode != NULL)
		{
			prev_of_slow->next = midnode;
			midnode->next = second_half;
		} else
		{
			prev_of_slow->next = second_half;
		}
	}
	return (res);
}
