#include "lists.h"
/**
 * insert_node - inserts at node
 * @head: pointer to head
 * @number: index to be inserted
 * Return: pointer to node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;

	if (head == NULL)
		return (NULL);
	while (*head != NULL)
	{
		if ((*head)->n <= number)
		{
			if ((*head)->next == NULL || number <= (*head)->next->n)
			{
				new = malloc(sizeof (listint_t));
				if (new == NULL)
					return (NULL);
				new->n = number;
				new->next = (*head)->next;
				(*head)->next = new;
				return (new);
			}
		}
		*head = (*head)->next;
	}
	return (NULL);
}
