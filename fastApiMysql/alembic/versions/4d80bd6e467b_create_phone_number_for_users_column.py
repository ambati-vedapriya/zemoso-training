"""Create phone number for users column

Revision ID: 4d80bd6e467b
Revises: 
Create Date: 2024-02-19 10:44:08.976130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4d80bd6e467b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(length=20), nullable=True))
    


def downgrade() -> None:
    pass
