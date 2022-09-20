#include "lists.h"
/**
 * insert_node - inserts at node
 * @head: pointer to head
 * @number: index to be inserted
 * Return: pointer to node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *i = *head, *j = *head;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof (listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
	}
	else
	{
		while (1)
		{
			if (j->n <= number <= i->n || i == NULL)
			{
				new->next = i;
				j->next = new;
				return (new);
			}
			j = i;
			i = i->next;
		}
	}
}
