// src/components/TodoApp.test.jsx

import { render, screen, within } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi } from 'vitest';
import TodoApp from './TodoApp';
import Swal from 'sweetalert2';

// Mock da biblioteca sweetalert2
vi.mock('sweetalert2', () => ({
    default: {
        fire: vi.fn(),
    },
}));

describe('TodoApp Component', () => {
    it('deve renderizar corretamente o estado inicial', () => {
        render(<TodoApp />);
        expect(screen.getByRole('heading', { name: /lista de tarefas/i })).toBeInTheDocument();
        expect(screen.getByPlaceholderText('adicione uma tarefa')).toBeInTheDocument();
        expect(screen.getByRole('button', { name: /adicionar/i })).toBeInTheDocument();
        expect(screen.getByText('não ha tarefas')).toBeInTheDocument();
    });

    it('deve permitir ao usuário adicionar uma nova tarefa', async () => {
        const user = userEvent.setup();
        render(<TodoApp />);

        const inputElement = screen.getByPlaceholderText('adicione uma tarefa');
        const addButton = screen.getByRole('button', { name: /adicionar/i });

        await user.type(inputElement, 'Comprar pão');
        await user.click(addButton);

        expect(screen.getByText('Comprar pão')).toBeInTheDocument();
        expect(inputElement.value).toBe('');
        expect(screen.queryByText('não ha tarefas')).not.toBeInTheDocument();
    });

    it('deve permitir ao usuário excluir uma tarefa', async () => {
        const user = userEvent.setup();
        render(<TodoApp />);

        const inputElement = screen.getByPlaceholderText('adicione uma tarefa');
        const addButton = screen.getByRole('button', { name: /adicionar/i });
        await user.type(inputElement, 'Levar o lixo para fora');
        await user.click(addButton);

        const addedTask = screen.getByText('Levar o lixo para fora');
        const deleteButton = within(addedTask.closest('li')).getByRole('button', { name: /excluir tarefa/i });
        await user.click(deleteButton);

        expect(screen.queryByText('Levar o lixo para fora')).not.toBeInTheDocument();
        expect(screen.getByText('não ha tarefas')).toBeInTheDocument();
    });

    it('não deve adicionar uma tarefa vazia e deve chamar o SweetAlert', async () => {
        const user = userEvent.setup();
        render(<TodoApp />);

        const addButton = screen.getByRole('button', { name: /adicionar/i });

        await user.click(addButton);

        expect(Swal.fire).toHaveBeenCalledWith({
            title: 'Calma aí!',
            text: 'Você precisa digitar uma tarefa!',
            icon: 'warning',
            confirmButtonText: 'Ok'
        });

        expect(screen.getByText('não ha tarefas')).toBeInTheDocument();
    });
});