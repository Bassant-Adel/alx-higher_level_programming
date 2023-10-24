#include "lists.h"

/**
 * insert_node -> A function -> inserts number into sorted singly linked list
 *@head: It's (Head)
 *@number: It's Insert Number
 *Return: address of new node || (NULL)-> if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nnode, *cunode;

	if (head == NULL)
	{
		return (NULL);

	}	nnode = malloc(sizeof(listint_t));

	if (nnode == NULL)
	{
		return (NULL);

	}	nnode->n = number;
	nnode->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		nnode->next = *head;
		*head = nnode;
		return (nnode);

	}	cunode = *head;

	while (cunode->next != NULL && cunode->next->n < number)
	{
		cunode = cunode->next;

	}	nnode->next = cunode->next;
	cunode->next = nnode;
	return (nnode);
}
