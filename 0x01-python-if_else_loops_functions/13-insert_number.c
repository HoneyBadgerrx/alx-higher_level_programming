#include "lists.h"
/**
 * insert_node - inserts at node
 * @head: pointer to head
 * @number: index to be inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
	if (head == NULL)
		return;
	return (add_nodeint_end(head, number));
	return (NULL);
}
