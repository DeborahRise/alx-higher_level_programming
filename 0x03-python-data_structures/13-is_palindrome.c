#include "lists.h"

/**
 * is_palindrome - a function that checks for a palindrome
 * in a singly linked list
 * @head: head of the node
 * Return: 0 if not, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *turtle = *head;
	listint_t *hare = *head;
	listint_t *temp, *first_half, *second_half;

	if (!(*head) || !head || !((*head)->next))
		return (1);

	while (hare && hare->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;
	}


	hare = turtle->next;
	temp = NULL;
	turtle->next = NULL;

	while (hare && hare->next)
	{
		temp = hare;
		hare = hare->next;
		temp->next = second_half;
		second_half = temp;
	}
	first_half = *head;

	while (second_half)
	{
		if (second_half->n != first_half->n)
			return (0);
		if (second_half->next && first_half->next)
		{
			second_half = second_half->next;
			first_half = first_half->next;
		}
		else
		{
			second_half = NULL;
			first_half = NULL;
		}
	}
	return (1);
}
