"""empty message

Revision ID: 14869e6ee737
Revises: 
Create Date: 2020-04-29 22:12:13.144577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14869e6ee737'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('encoded_image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Images')
    # ### end Alembic commands ###
