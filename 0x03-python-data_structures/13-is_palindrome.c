#include "lists.h"

/**
 * is_palindrome - checks linked list is a palindrome
 *@head: A double pointer to head of a singly linked list of int
 *Return: (1) || (0)
 */

int is_palindrome(listint_t **head)
{
	int check_palindrome = 1;
	listint_t *prev = NULL;
	listint_t *nnode;
	listint_t *slPtr = *head;
	listint_t *fastPtr = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (check_palindrome);

	while (fastPtr != NULL && fastPtr->next != NULL)
	{
		fastPtr = fastPtr->next->next;
		nnode = slPtr;
		slPtr = slPtr->next;
		nnode->next = prev;
		prev = nnode;
	}

	if (fastPtr != NULL)
		slPtr = slPtr->next;
	while (slPtr != NULL)
	{
		if (prev->n != slPtr->n)
		{
			check_palindrome = 0;
			break;
		}		prev = prev->next;
		slPtr = slPtr->next;
	} nnode = NULL;
	fastPtr = prev;
	while (fastPtr != NULL)
	{
		prev = fastPtr->next;
		fastPtr->next = nnode;
		nnode = fastPtr;
		fastPtr = prev;
	} *head = nnode;
	return (check_palindrome);
}
