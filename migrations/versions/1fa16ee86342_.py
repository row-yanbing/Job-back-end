"""empty message

Revision ID: 1fa16ee86342
Revises: dfa694f4994d
Create Date: 2020-04-22 10:18:55.373757

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1fa16ee86342'
down_revision = 'dfa694f4994d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job_signup', schema=None) as batch_op:
        batch_op.add_column(sa.Column('stuId', sa.BigInteger(), nullable=True, comment='申请学生的学生id号'))
        batch_op.alter_column('userId',
               existing_type=mysql.BIGINT(display_width=20),
               comment='申请学生的用户id号',
               existing_comment='申请学生的id号',
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job_signup', schema=None) as batch_op:
        batch_op.alter_column('userId',
               existing_type=mysql.BIGINT(display_width=20),
               comment='申请学生的id号',
               existing_comment='申请学生的用户id号',
               existing_nullable=True)
        batch_op.drop_column('stuId')

    # ### end Alembic commands ###
