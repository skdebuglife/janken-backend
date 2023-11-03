"""add published_at column

Revision ID: 88b9d1e9b32b
Revises: a9e9660843ab
Create Date: 2023-05-15 20:10:14.523184

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '88b9d1e9b32b'
down_revision = 'a9e9660843ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('published_at', sa.Date(), nullable=False, comment='book published date'))
    # op.drop_constraint('fk_books_author_id_authors', 'books', type_='foreignkey')
    # op.create_foreign_key(op.f('fk_books_author_id_authors'), 'books', 'authors', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_constraint(op.f('fk_books_author_id_authors'), 'books', type_='foreignkey')
    # op.create_foreign_key('fk_books_author_id_authors', 'books', 'authors', ['author_id'], ['id'])
    op.drop_column('books', 'published_at')
    # ### end Alembic commands ###
