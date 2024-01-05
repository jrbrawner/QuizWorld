"""inital quiz tables

Revision ID: 707df118cd44
Revises: 3f5917d89dc6
Create Date: 2024-01-04 19:40:45.939722

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '707df118cd44'
down_revision: Union[str, None] = '3f5917d89dc6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.create_table(
        'quiz',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('title')
    )

    op.create_table(
        'question',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('question_text', sa.String(), nullable=False),
        sa.Column('answer_text', sa.String(), nullable=False),
        sa.Column('correct_answer', sa.Integer(), nullable=False),
        sa.Column('quiz_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(('quiz_id', ), ['quiz.id'])
    )



def downgrade() -> None:
    op.drop_table('quiz')
    op.drop_table('question')
