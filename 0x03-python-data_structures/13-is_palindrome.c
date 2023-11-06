#include "lists.h"

/**
 * is_palindrome - a function that checks for a palindrome
 * in a singly linked list
 * @head: a double pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	listint_t *turtle = *head;
	listint_t *hare = *head;

	/* Find the middle of the linked list */
	while (hare && hare->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;
	}

	/* Reverse the second half of the linked list */
	listint_t *prev = NULL;
	listint_t *next = NULL;
	listint_t *current = turtle;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	listint_t *second_half = prev;
	listint_t *first_half = *head;

	/* Compare the first half and reversed second half */
	while (second_half)
	{
		if (second_half->n != first_half->n)
			return (0);
		second_half = second_half->next;
		first_half = first_half->next;
	}

	return (1);
}
