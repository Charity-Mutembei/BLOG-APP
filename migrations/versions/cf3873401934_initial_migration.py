"""Initial Migration

Revision ID: cf3873401934
Revises: 79081df7545a
Create Date: 2022-05-18 08:41:11.867475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf3873401934'
down_revision = '79081df7545a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('commenter_name', sa.String(), nullable=True))
    op.add_column('comments', sa.Column('blog_review', sa.String(), nullable=True))
    op.add_column('comments', sa.Column('posted', sa.DateTime(), nullable=True))
    op.add_column('comments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('comments_blog_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.drop_column('comments', 'name')
    op.drop_column('comments', 'blog_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('blog_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_blog_id_fkey', 'comments', 'roles', ['blog_id'], ['id'])
    op.drop_column('comments', 'user_id')
    op.drop_column('comments', 'posted')
    op.drop_column('comments', 'blog_review')
    op.drop_column('comments', 'commenter_name')
    # ### end Alembic commands ###