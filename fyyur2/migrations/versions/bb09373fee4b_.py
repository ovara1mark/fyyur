"""empty message

Revision ID: bb09373fee4b
Revises: 532181fdf315
Create Date: 2022-05-25 22:30:19.792011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb09373fee4b'
down_revision = '532181fdf315'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('website_link', sa.String(length=120), nullable=False))
    op.add_column('venue', sa.Column('seeking_talent', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'seeking_talent')
    op.drop_column('venue', 'website_link')
    # ### end Alembic commands ###
