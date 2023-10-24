#include "lists.h"

/**
 * check_cycle - A function that checks -> singly linked list has cycle
 *@list: It's refer -> arg 1
 *Return: (0)-> if it is no cycle & (1)-> if it is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *cc = list, *xx = list;

	if (list == NULL)
		return (0);
	cc = list->next;
	xx = list;

	while (cc != NULL && cc->next != NULL)
	{
		xx = xx->next;
		cc = cc->next->next;

		if (xx == cc)
			return (1);

	}	return (0);
}
