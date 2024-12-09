"""Create table search

Revision ID: 52c0628f5bfe
Revises: 
Create Date: 2024-12-11 01:06:23.988978

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52c0628f5bfe'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('search',
    sa.Column('telegram_id', sa.BigInteger(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('date', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('full_name'),
    sa.UniqueConstraint('telegram_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('search')
    # ### end Alembic commands ###
