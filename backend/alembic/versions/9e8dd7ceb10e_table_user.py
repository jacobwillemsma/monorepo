"""table_user

Revision ID: 9e8dd7ceb10e
Revises: 
Create Date: 2021-01-02 20:18:49.000581

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9e8dd7ceb10e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=True),
                    sa.Column('first_name', sa.String(), nullable=True),
                    sa.Column('last_name', sa.String(), nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))


def downgrade():
    op.drop_table('user')
