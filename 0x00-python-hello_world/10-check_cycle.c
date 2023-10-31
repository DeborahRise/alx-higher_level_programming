#include "lists.h"

/**
 * check_cycle - a function that checks
 * for the loop in a linked list
 * @list: pointer of type struct
 * Return: 0 if no cycle, 1 if cycle exists
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle;
	listint_t *hare;

	if (list == NULL || list->next == NULL)
		return  (0);

	turtle = list->next;
	hare = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare->next)
		{
			return (1);
		}
		turtle = turtle->next;
		hare = hare->next->next;
	}
	return (0);
}
