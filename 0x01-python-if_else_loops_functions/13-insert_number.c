#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - insert a number sorted in a list
 * @head: head of list
 * @number: number to be inserted
 * Return: the address of the new node, NULL on fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (temp == NULL || temp->n >= number)
	{
		new->next = temp;
		temp = new;
		return (new);
	}


	while (temp->next && temp->next->n <  number)
	{
		temp = temp->next;
	}
	new->next = temp->next;
	temp->next = new;

	return (new);
}
