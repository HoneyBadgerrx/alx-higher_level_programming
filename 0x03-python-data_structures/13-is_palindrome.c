#include "lists.h"
/**
 * is_palindrome - checks fo rpalin
 * @head: pointer to ead
 * Return: 0 if not, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *p = *head, *q = *head;
	int count = 0, i, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	for (; q->next; count++)
		q = q->next;
	for (i = 0;; ++i)
	{
		q = *head;
		for (j = 0; j < count - i; ++j)
			q = q->next;
		if (i > j || j == i)
			return (1);
		if (q->n != p->n)
			break;
		p = p->next;
	}
	return (0);
}
