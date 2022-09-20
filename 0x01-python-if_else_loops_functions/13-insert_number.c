#include "lists.h"
/**
 * insert_node - inserts at node
 * @head: pointer to head
 * @number: index to be inserted
 * Return: pointer to node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *i = *head;

	if (head == NULL)
		return (NULL);
	while (i != NULL)
	{
		if (i->n <= number)
		{
			if (i->next == NULL || number <= i->next->n)
			{
				new = malloc(sizeof (listint_t));
				if (new == NULL)
					return (NULL);
				new->n = number;
				new->next = i->next;
				i->next = new;
				return (new);
			}
		}
		i = i->next;
	}
	return (NULL);
}
