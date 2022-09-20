#include "lists.h"
/**
 * insert_node - inserts node
 * @head: pointer to list
 * @number: number in strut
 * Return: NULL on failure or pointer to created node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *i = *head;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	else if (number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (1)
		{
			if (i->next == NULL || (number >= i->n && number <= i->next->n))
			{
				new->next = i->next;
				i->next = new;
				return (new);
			}
			i = i->next;
		}
	}
	return (NULL);
}
