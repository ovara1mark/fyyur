"""empty message

Revision ID: e78a45dcde20
Revises: 651ea93259e4
Create Date: 2022-05-27 22:25:48.779491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e78a45dcde20'
down_revision = '651ea93259e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'show', 'artist', ['artist_id'], ['id'])
    op.create_foreign_key(None, 'show', 'venue', ['venue_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'show', type_='foreignkey')
    op.drop_constraint(None, 'show', type_='foreignkey')
    # ### end Alembic commands ###