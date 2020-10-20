"""create products table

Revision ID: d591cd5964e3
Revises: 016712d9f3f4
Create Date: 2020-10-20 13:30:07.654834

"""
from alembic import op
import sqlalchemy as sa
from app.utils.uuid import generate_uuid


# revision identifiers, used by Alembic.
revision = 'd591cd5964e3'
down_revision = '016712d9f3f4'
branch_labels = None
depends_on = None


def upgrade():
    prs = op.create_table(
        'products',
        sa.Column('id', sa.String(50), primary_key=True, index=True),
        sa.Column('slug', sa.String(191),
                  unique=True,
                  index=True,
                  nullable=False),
        sa.Column('name', sa.String(191),
                  unique=True,
                  index=True,
                  nullable=False),
        sa.Column('is_active', sa.Boolean, default=True),
        sa.Column('category_id', sa.String(50), default=True),
        sa.Column('insurance_type_id', sa.String(50), default=True),
        sa.Column('featured', sa.Boolean, default=True),
        sa.Column('premium_type', sa.String(100)),
        sa.Column('bundling_with_rider', sa.Boolean, default=True),
        sa.Column('created_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
    )

    pr_categories = op.create_table(
        'product_categories',
        sa.Column('id', sa.String(50), primary_key=True, index=True),
        sa.Column('name', sa.String(191),
                  unique=True,
                  index=True,
                  nullable=False),
        sa.Column('created_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
    )

    pr_insurance_types = op.create_table(
        'product_insurance_types',
        sa.Column('id', sa.String(50), primary_key=True, index=True),
        sa.Column('name', sa.String(191),
                  unique=True,
                  index=True,
                  nullable=False),
        sa.Column('created_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
    )

    pr_details = op.create_table(
        'product_details',
        sa.Column('id', sa.String(50), primary_key=True, index=True),
        sa.Column('summary', sa.String(191),
                  unique=True,
                  index=True,
                  nullable=False),
        sa.Column('description', sa.String(255)),
        sa.Column('icon', sa.String(255)),
        sa.Column('coverage_period', sa.String(191)),
        sa.Column('basic_id', sa.String(50)),
        sa.Column('rider_id', sa.String(50)),
        sa.Column('created_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
    )

    pr_benefits = op.create_table(
        'product_benefits',
        sa.Column('id', sa.String(50), primary_key=True, index=True),
        sa.Column('product_id', sa.String(50)),
        sa.Column('name', sa.String(191),
                  nullable=False),
        sa.Column('benefit', sa.String(255)),
        sa.Column('icon', sa.String(255)),
        sa.Column('created_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
    )

    pr_riders = op.create_table(
        'product_riders',
        sa.Column('id', sa.String(50), primary_key=True, index=True),
        sa.Column('slug', sa.String(191),
                  unique=True,
                  index=True,
                  nullable=False),
        sa.Column('name', sa.String(191),
                  unique=True,
                  index=True,
                  nullable=False),
        sa.Column('is_active', sa.Boolean, default=True),
        sa.Column('category_id', sa.String(50), default=True),
        sa.Column('insurance_type_id', sa.String(50), default=True),
        sa.Column('basic_id', sa.String(50), default=True),
        sa.Column('premium_type', sa.String(100)),
        sa.Column('created_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
    )

    pr_plans = op.create_table(
        'product_plans',
        sa.Column('id', sa.String(50), primary_key=True, index=True),
        sa.Column('name', sa.String(191),
                  index=True,
                  nullable=False),
        sa.Column('product_id', sa.String(50), nullable=False),
        sa.Column('product_code', sa.String(50), nullable=False),
        sa.Column('rider_id', sa.String(50), nullable=False),
        sa.Column('product_plan_code', sa.String(50),
                  index=True,
                  nullable=False),
        sa.Column('icon', sa.String(255)),
        sa.Column('sum_assured', sa.Integer),
        sa.Column('discount', sa.Integer),
        sa.Column('discount', sa.Integer),
        sa.Column('type', sa.String(191)),
        sa.Column('monthly_premium', sa.Integer),
        sa.Column('yearly_premium', sa.Integer),

        sa.Column('created_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
    )

    # Seed Data
    pr_categories_id_1 = generate_uuid()
    pr_categories_id_2 = generate_uuid()
    op.bulk_insert(pr_categories,
                   [
                        {'id': pr_categories_id_1,
                         'name': 'Partner Product', },
                        {'id': pr_categories_id_2,
                         'name': 'Original Product', },
                    ])

    pr_insurance_types_id_1 = generate_uuid()
    pr_insurance_types_id_2 = generate_uuid()
    pr_insurance_types_id_3 = generate_uuid()
    pr_insurance_types_id_4 = generate_uuid()
    pr_insurance_types_id_5 = generate_uuid()
    pr_insurance_types_id_6 = generate_uuid()
    op.bulk_insert(pr_insurance_types,
                   [
                        {'id': pr_insurance_types_id_1,
                         'name': 'Asuransi Jiwa + Kecelakaan', },
                        {'id': pr_insurance_types_id_2,
                         'name': 'Asuransi Jiwa + Penyakit Kritis', },
                        {'id': pr_insurance_types_id_3,
                         'name': 'Asuransi Jiwa', },
                        {'id': pr_insurance_types_id_4,
                         'name': 'Asuransi Kecelakaan Kendaraan Bermotor', },
                        {'id': pr_insurance_types_id_5,
                         'name': 'Asuransi Kecelakaan saat Liburan', },
                        {'id': pr_insurance_types_id_6,
                         'name': 'Asuransi Jiwa + Kesehatan', },
                    ])

    prs_id_1 = generate_uuid()
    prs_id_2 = generate_uuid()
    prs_id_3 = generate_uuid()
    prs_id_4 = generate_uuid()
    prs_id_5 = generate_uuid()
    op.bulk_insert(prs,
                   [
                        {
                            "id": prs_id_1,
                            "slug": "super-life-protection",
                            "name": "Super Life Protection",
                            "is_active": 1,
                            "category_id": pr_categories_id_2,
                            "insurance_type_id": pr_insurance_types_id_3,
                            "featured": 0,
                            "premium_type": "rate by age",
                            "bundling_with_rider": 0,
                        },
                        {
                            "id": prs_id_2,
                            "slug": "super-strong-protection",
                            "name": "Super Strong Protection",
                            "is_active": 1,
                            "category_id": pr_categories_id_2,
                            "insurance_type_id": pr_insurance_types_id_2,
                            "featured": 0,
                            "premium_type": "rate by age",
                            "bundling_with_rider": 1,
                        },
                        {
                            "id": prs_id_3,
                            "slug": "super-safe-protection",
                            "name": "Super Safe Protection",
                            "is_active": 1,
                            "category_id": pr_categories_id_1,
                            "insurance_type_id": pr_insurance_types_id_1,
                            "featured": 1,
                            "premium_type": "fixed price",
                            "bundling_with_rider": 0,
                        },
                        {
                            "id": prs_id_4,
                            "slug": "my-hospital-protection",
                            "name": "My Hospital Protection",
                            "is_active": 1,
                            "category_id": pr_categories_id_2,
                            "insurance_type_id": pr_insurance_types_id_6,
                            "featured": 0,
                            "premium_type": "rate by age",
                            "bundling_with_rider": 0,
                        },
                        {
                            "id": prs_id_5,
                            "slug": "super-care-protection",
                            "name": "Super Care Protection",
                            "is_active": 1,
                            "category_id": pr_categories_id_2,
                            "insurance_type_id": pr_insurance_types_id_6,
                            "featured": 0,
                            "premium_type": "rate by age",
                            "bundling_with_rider": 0,
                        }
                   ])

    pr_riders_id_1 = generate_uuid()
    pr_riders_id_2 = generate_uuid()
    pr_riders_id_3 = generate_uuid()
    op.bulk_insert(pr_riders,
                   [
                        {
                            "id": pr_riders_id_1,
                            "slug": "super-motor-protection",
                            "name": "Super Motor Protection",
                            "category_id": pr_categories_id_1,
                            "insurance_type_id": pr_insurance_types_id_4,
                            "basic_id": prs_id_3,
                            "premium_type": "fixed price",
                        },
                        {
                            "id": pr_riders_id_2,
                            "slug": "super-holiday-protection",
                            "name": "Super Holiday Protection",
                            "category_id": pr_categories_id_1,
                            "insurance_type_id": pr_insurance_types_id_5,
                            "basic_id": prs_id_3,
                            "premium_type": "fixed price",
                        },
                        {
                            "id": pr_riders_id_3,
                            "slug": "super-strong-protection-rider",
                            "name": "Super Strong Protection Rider",
                            "category_id": pr_categories_id_2,
                            "insurance_type_id": pr_insurance_types_id_2,
                            "basic_id": prs_id_2,
                            "premium_type": "rate by age",
                        }
                    ])

    pr_plans_1 = generate_uuid()
    pr_plans_2 = generate_uuid()
    pr_plans_3 = generate_uuid()
    pr_plans_4 = generate_uuid()
    pr_plans_5 = generate_uuid()
    pr_plans_6 = generate_uuid()
    pr_plans_7 = generate_uuid()
    pr_plans_8 = generate_uuid()
    pr_plans_9 = generate_uuid()
    pr_plans_10 = generate_uuid()
    pr_plans_11 = generate_uuid()
    pr_plans_12 = generate_uuid()
    pr_plans_13 = generate_uuid()
    pr_plans_14 = generate_uuid()
    pr_plans_15 = generate_uuid()
    pr_plans_16 = generate_uuid()
    pr_plans_17 = generate_uuid()
    pr_plans_18 = generate_uuid()
    pr_plans_19 = generate_uuid()
    pr_plans_20 = generate_uuid()
    pr_plans_21 = generate_uuid()
    pr_plans_22 = generate_uuid()
    op.bulk_insert(
        pr_plans,
        [
            {
                "id": pr_plans_1,
                "product_id": prs_id_1,
                "rider_id": "",
                "product_plan_code": "DLP1_Bronze_Plan",
                "product_code": "DLP1",
                "icon": "products/plans/"
                + "Tc7vZDmle0qLgVIGHdSIomMXqrnsQGBEMKCEK6Sr.svg",
                "name": "Bronze Plan",
                "description": "<div>Asuransi untuk kamu yang ingin memulai"
                + " perlindungan dengan premi yang terjangkau</div>",
                "sum_assured": 100000000,
                "discount": 100,
                "type": "basic",
                "monthly_premium": 0,
                "yearly_premium": 0,
            },
            {
                "id": pr_plans_2,
                "product_id": prs_id_1,
                "rider_id": "",
                "product_plan_code": "DLP1_Silver_Plan",
                "product_code": "DLP1",
                "icon": "products/plans/"
                + "rri8V6pucvjMLvkU0Ub3r8tZYGQmcsQhiLY3BJNH.svg",
                "name": "Silver Plan",
                "description": "<div>Asuransi untuk kamu yang tahu pentingnya"
                + " manfaat perlindungan diri yang lebih dalam hidup</div>",
                "sum_assured": 200000000,
                "discount": 80,
                "type": "basic",
                "monthly_premium": 0,
                "yearly_premium": 0,
            },
            {
                "id": pr_plans_3,
                "product_id": prs_id_1,
                "rider_id": "",
                "product_plan_code": "DLP1_Gold_Plan",
                "product_code": "DLP1",
                "icon": "products/plans/"
                + "TbIn6IOOGtvY30E7HAtCs2IolmCftDzaQ4ESPCF3.svg",
                "name": "Gold Plan",
                "description": "<div>Asuransi untuk kamu yang ingin memberikan"
                + " perlindungan yang terbaik kepada orang terkasih dan diri"
                + " sendiri</div>",
                "sum_assured": 300000000,
                "discount": 78,
                "type": "basic",
                "monthly_premium": 0,
                "yearly_premium": 0,
            },
            {
                "id": pr_plans_4,
                "product_id": prs_id_2,
                "rider_id": "",
                "product_plan_code": "DCP1_Bronze_Plan",
                "product_code": "DCP1",
                "icon": "products/plans/"
                + "CJgTzOpljlUZvJeM4LIlJwZZKvc8Orm2Q88Lyr8e.svg",
                "name": "Bronze Plan",
                "description": "<div>Asuransi untuk kamu yang ingin kuat"
                + " selalu dalam menjalani hari dengan perlindungan tanpa"
                + " harus menguras kantong</div>",
                "sum_assured": 100000000,
                "discount": 0,
                "type": "basic",
                "monthly_premium": 0,
                "yearly_premium": 0,
            },
            {
                "id": pr_plans_5,
                "product_id": prs_id_2,
                "rider_id": "",
                "product_plan_code": "DCP1_Silver_Plan",
                "product_code": "DCP1",
                "icon": "products/plans/"
                + "1mYa8fceRvaGUwCS7Lo892hdJIyE8ueJcx17JrZg.svg",
                "name": "Silver Plan",
                "description": "<div>Asuransi untuk kamu pribadi yang"
                + " memprioritaskan kesehatan untuk menjalani hidup dengan"
                + " kuat</div>",
                "sum_assured": 200000000,
                "discount": 0,
                "type": "basic",
                "monthly_premium": 0,
                "yearly_premium": 0,
            },
            {
                "id": pr_plans_6,
                "product_id": prs_id_2,
                "rider_id": "",
                "product_plan_code": "DCP1_Gold_Plan",
                "product_code": "DCP1",
                "icon": "products/plans/"
                + "ixLR6BJKL2YKWfOkfZNPK9cVFPYRE2Kb96RK8FlX.svg",
                "name": "Gold Plan",
                "description": "<div>Asuransi untuk kamu yang menginginkan"
                + " perlindungan maksimal untuk menjadi siap menghadapi"
                + " hal-hal tidak terduga</div>",
                "sum_assured": 300000000,
                "discount": 0,
                "type": "basic",
                "monthly_premium": 0,
                "yearly_premium": 0,
            },
            {
                "id": pr_plans_7,
                "product_id": prs_id_2,
                "rider_id": pr_riders_id_3,
                "product_plan_code": "DCPR_Bronze_Plan",
                "product_code": "DCPR",
                "icon": "",
                "name": "Bronze Plan",
                "description": "",
                "sum_assured": 100000000,
                "discount": 0,
                "type": "rider",
                "monthly_premium": 0,
                "yearly_premium": 0,
            },
            {
                "id": pr_plans_8,
                "product_id": prs_id_2,
                "rider_id": pr_riders_id_3,
                "product_plan_code": "DCPR_Silver_Plan",
                "product_code": "DCPR",
                "icon": "",
                "name": "Silver Plan",
                "description": "",
                "sum_assured": 200000000,
                "discount": 0,
                "type": "rider",
                "monthly_premium": 0,
                "yearly_premium": 0,
            },
            {
                "id": pr_plans_9,
                "product_id": prs_id_2,
                "rider_id": pr_riders_id_3,
                "product_plan_code": "DCPR_Gold_Plan",
                "product_code": "DCPR",
                "icon": "",
                "name": "Gold Plan",
                "description": "",
                "sum_assured": 300000000,
                "discount": 0,
                "type": "rider",
                "monthly_premium": 0,
                "yearly_premium": 0,
            },
            {
                "id": pr_plans_10,
                "product_id": prs_id_3,
                "rider_id": "",
                "product_plan_code": "DSS1_Bronze_Plan",
                "product_code": "DSS1",
                "icon": "products/plans/"
                + "EECIKhCA6mxfQor2fpeshOn8NYFAuBP0SClq6ZZJ.svg",
                "name": "Bronze Plan",
                "description": "<div>Asuransi untuk kamu yang baru memulai"
                + " hidup mandiri, ingin mencoba banyak hal, dan mendapatkan"
                + " manfaat perlindungan tanpa menguras kantong</div>",
                "sum_assured": 200000000,
                "discount": 0,
                "type": "basic",
                "monthly_premium": 36500,
                "yearly_premium": 403000,
            },
            {
                "id": pr_plans_11,
                "product_id": prs_id_3,
                "rider_id": "",
                "product_plan_code": "DSS2_Silver_Plan",
                "product_code": "DSS2",
                "icon": "products/plans/"
                + "f8LYWIkKru2VlpBt4JhP0Mv9moenfItdnNKTRv59.svg",
                "name": "Silver Plan",
                "description": "<div>Asuransi untuk kamu yang punya aktivitas"
                + " segudang, dan membutuhkan perlindungan lebih untuk"
                + " menggapai mimpi-mimpimu</div>",
                "sum_assured": 500000000,
                "discount": 0,
                "type": "basic",
                "monthly_premium": 91000,
                "yearly_premium": 1007000,
            },
            {
                "id": pr_plans_12,
                "product_id": prs_id_3,
                "rider_id": "",
                "product_plan_code": "DSS3_Gold_Plan",
                "product_code": "DSS3",
                "icon": "products/plans/"
                + "r6A7n1T1YJTQgZk8GoLeqYhLaFRcVazllo7t4VKv.svg",
                "name": "Gold Plan",
                "description": "<div>Asuransi untuk kamu yang selalu total"
                + " dalam menekuni hobi dan suka tantangan</div>",
                "sum_assured": 1000000000,
                "discount": 0,
                "type": "basic",
                "monthly_premium": 181500,
                "yearly_premium": 2013500,
            },
            {
                "id": pr_plans_13,
                "product_id": prs_id_3,
                "rider_id": pr_riders_id_1,
                "product_plan_code": "DSMR1_Bronze_Plan",
                "product_code": "DSMR1",
                "icon": "products/plans/"
                + "mOQie7wotHo7yWJkJurSAye3qDv6W2buQfrSFdXI.svg",
                "name": "Bronze Plan",
                "description": "",
                "sum_assured": 10000000,
                "discount": 0,
                "type": "rider",
                "monthly_premium": 9500,
                "yearly_premium": 105000,
            },
            {
                "id": pr_plans_14,
                "product_id": prs_id_3,
                "rider_id": pr_riders_id_1,
                "product_plan_code": "DSMR2_Silver_Plan",
                "product_code": "DSMR2",
                "icon": "products/plans/"
                + "7h1Rn2pRlGhbowpLNEc2oEMrg31LbYptW09pv6MA.svg",
                "name": "Silver Plan",
                "description": "",
                "sum_assured": 25000000,
                "discount": 0,
                "type": "rider",
                "monthly_premium": 24000,
                "yearly_premium": 262500,
            },
            {
                "id": pr_plans_15,
                "product_id": prs_id_3,
                "rider_id": pr_riders_id_1,
                "product_plan_code": "DSMR3_Gold_Plan",
                "product_code": "DSMR3",
                "icon": "products/plans/"
                + "vWAjsMebTrVCGW6pKhJFYE0sgomXrGNs2luN7p7w.svg",
                "name": "Gold Plan",
                "description": "",
                "sum_assured": 50000000,
                "discount": 0,
                "type": "rider",
                "monthly_premium": 47500,
                "yearly_premium": 525000,
            },
            {
                "id": pr_plans_16,
                "product_id": prs_id_3,
                "rider_id": pr_riders_id_2,
                "product_plan_code": "DSHR1_Bronze_Plan",
                "product_code": "DSHR1",
                "icon": "products/plans/"
                + "b5GkdmMKVwcBy8AbpZrQNaQKYiLUpFVdj0tPGiaL.svg",
                "name": "Bronze Plan",
                "description": "",
                "sum_assured": 200000000,
                "discount": 0,
                "type": "rider",
                "monthly_premium": 21000,
                "yearly_premium": 233000,
            },
            {
                "id": pr_plans_17,
                "product_id": prs_id_3,
                "rider_id": pr_riders_id_2,
                "product_plan_code": "DSHR2_Silver_Plan",
                "product_code": "DSHR2",
                "icon": "products/plans/"
                + "90o9z2mc8x0Xsrw7P6xnqTfIUC5haS5Zk5YJ5TX6.svg",
                "name": "Silver Plan",
                "description": "",
                "sum_assured": 500000000,
                "discount": 0,
                "type": "rider",
                "monthly_premium": 52500,
                "yearly_premium": 582000,
            },
            {
                "id": pr_plans_18,
                "product_id": prs_id_3,
                "rider_id": pr_riders_id_2,
                "product_plan_code": "DSHR3_Gold_Plan",
                "product_code": "DSHR3",
                "icon": "products/plans/"
                + "q6osdJiJcS932Lg1unz1eOnAP8w4wbt3teO0mcW7.svg",
                "name": "Gold Plan",
                "description": "",
                "sum_assured": 1000000000,
                "discount": 0,
                "type": "rider",
                "monthly_premium": 105000,
                "yearly_premium": 1164000,
            },
            {
                "id": pr_plans_19,
                "product_id": prs_id_4,
                "rider_id": "",
                "product_plan_code": "DHP1_Bronze_Plan",
                "product_code": "DHP1",
                "icon": "products/plans/"
                + "qxN6aaNSBWn9K3AB23bLZaZ4MR7KfMAZDHlsmAC0.svg",
                "name": "Bronze Plan",
                "description": "<div>Produk unggulan yang meringankan beban"
                + " biaya perawatan Rumah Sakit, baik rawat inap maupun ICU"
                + ".</div>",
                "sum_assured": 20000000,
                "discount": 100,
                "type": "basic",
                "monthly_premium": 0,
                "yearly_premium": 0,
            },
            {
                "id": pr_plans_20,
                "product_id": prs_id_4,
                "rider_id": "",
                "product_plan_code": "DHP1_Silver_Plan",
                "product_code": "DHP1",
                "icon": "products/plans/"
                + "z5o5xUTThFOVyEtnHcdSD04UYLgQLKKnK3erGYZx.svg",
                "name": "Silver Plan",
                "description": "<div>Produk unggulan yang meringankan beban"
                + " biaya perawatan Rumah Sakit, baik rawat inap maupun ICU"
                + ".</div>",
                "sum_assured": 30000000,
                "discount": 88,
                "type": "basic",
                "monthly_premium": 0,
                "yearly_premium": 0,
            },
            {
                "id": pr_plans_21,
                "product_id": prs_id_4,
                "rider_id": "",
                "product_plan_code": "DHP1_Gold_Plan",
                "product_code": "DHP1",
                "icon": "products/plans/"
                + "aNYUnQwKaJG9HMhlCwWTPOqvV6elZTrvYkDzaxHN.svg",
                "name": "Gold Plan",
                "description": "<div>Produk unggulan yang meringankan beban"
                + " biaya perawatan Rumah Sakit, baik rawat inap maupun ICU"
                + ".</div>",
                "sum_assured": 40000000,
                "discount": 84,
                "type": "basic",
                "monthly_premium": 0,
                "yearly_premium": 0,
            },
            {
                "id": pr_plans_22,
                "product_id": prs_id_4,
                "rider_id": "",
                "product_plan_code": "DHP1_Gold_Plus",
                "product_code": "DHP1",
                "icon": "products/plans/"
                + "C85tyAqh9edtSMnhqr3sw7gYNCT2tCRwKMDMioYH.svg",
                "name": "Gold Plus",
                "description": "<div>Produk unggulan yang meringankan beban"
                + " biaya perawatan Rumah Sakit, baik rawat inap maupun ICU"
                + ".</div>",
                "sum_assured": 50000000,
                "discount": 78,
                "type": "basic",
                "monthly_premium": 0,
                "yearly_premium": 0,
            }
        ])

    pr_benefits_id_1 = generate_uuid()
    pr_benefits_id_2 = generate_uuid()
    pr_benefits_id_3 = generate_uuid()
    pr_benefits_id_4 = generate_uuid()
    pr_benefits_id_5 = generate_uuid()
    pr_benefits_id_6 = generate_uuid()
    pr_benefits_id_7 = generate_uuid()
    pr_benefits_id_8 = generate_uuid()
    pr_benefits_id_9 = generate_uuid()
    pr_benefits_id_10 = generate_uuid()
    pr_benefits_id_11 = generate_uuid()
    pr_benefits_id_12 = generate_uuid()
    pr_benefits_id_13 = generate_uuid()
    pr_benefits_id_14 = generate_uuid()
    op.bulk_insert(
        pr_benefits,
        [
            {
                "id": pr_benefits_id_1,
                "product_id": prs_id_1,
                "icon": "products/benefits/"
                + "5aa0080aafe315bd4bc1173785db9ed51973dcbe.svg",
                "name": "Premi yang Terjangkau",
                "benefit": "<div>Dapatkan perlindungan maksimal dengan biaya"
                + " premi yang super terjangkau</div>",
            },
            {
                "id": pr_benefits_id_2,
                "product_id": prs_id_1,
                "icon": "products/benefits/"
                + "3f13e9d47e5d1cf773841f609edcf66dff9cb2e2.svg",
                "name": "Jaminan Uang Pertanggungan Menyeluruh",
                "benefit": "<div>100% uang pertanggungan jika"
                + " yang tertanggung tutup usia dalam masa asuransi."
                + " Ahli Waris juga akan mendapat 100% uang pertanggungan jika"
                + " yang tertanggung tutup usia dikarenakan penyakit kritis di"
                + " tahun pertama masa asuransi</div>",
            },
            {
                "id": pr_benefits_id_3,
                "product_id": prs_id_1,
                "icon": "products/benefits/"
                + "25132ae6a4f4982b3cf2894e126c55620e239246.svg",
                "name": "2x Jaminan Uang Pertanggungan Kecelakaan",
                "benefit": "<div>Ahli Waris akan mendapat 200"
                + "% uang pertanggungan jika yang tertanggung tutup usia"
                + " karena kecelakaan di dalam masa asuransi</div>",
            },
            {
                "id": pr_benefits_id_4,
                "product_id": prs_id_1,
                "icon": "products/benefits/"
                + "601864a56db5e057e9ecf9964b5e0d0a049d5e46.svg",
                "name": "Perlindungan Optimal Cacat Total dan Tetap",
                "benefit": "<div>100% uang pertanggungan jika"
                + " terjadi kecelakaan dan mengalami cacat total dan tetap"
                + "</div>",
            },
            {
                "id": pr_benefits_id_5,
                "product_id": prs_id_2,
                "icon": "products/benefits/"
                + "5aa0080aafe315bd4bc1173785db9ed51973dcbe.svg",
                "name": "Asuransi Penyakit Kritis Super Terjangkau",
                "benefit": "<div>Dapat manfaat perlindungan penyakit kritis"
                + " dengan premi asuransi super terjangkau</div>",
            },
            {
                "id": pr_benefits_id_6,
                "product_id": prs_id_2,
                "icon": "products/benefits/"
                + "3f13e9d47e5d1cf773841f609edcf66dff9cb2e2.svg",
                "name": "Jaminan Uang Pertanggungan Menyeluruh",
                "benefit": "<div>100% uang pertanggungan jika"
                + " yang tertanggung tutup usia dalam masa asuransi. Ahli"
                + " waris juga akan mendapat 100% pengembalian premi jika yang"
                + " tertanggung tutup usia dikarenakan penyakit kritis</div>",
            },
            {
                "id": pr_benefits_id_7,
                "product_id": prs_id_2,
                "icon": "products/benefits/"
                + "25132ae6a4f4982b3cf2894e126c55620e239246.svg",
                "name": "Perlindungan Optimal Penyakit Kritis",
                "benefit": "<div>Tertanggung akan mendapat 100%"
                + " manfaat perlindungan super jika terkena penyakit kritis"
                + " setelah masa tunggu selama 12 bulan dan selama masa"
                + " asuransi</div>",
            },
            {
                "id": pr_benefits_id_8,
                "product_id": prs_id_3,
                "icon": "products/benefits/"
                + "5aa0080aafe315bd4bc1173785db9ed51973dcbe.svg",
                "name": "Tarif Flat Sepanjang Tahun",
                "benefit": "<div>Bayar premi dengan harga yang"
                + " tak pernah berubah selama masa asuransi kamu</div>",
            },
            {
                "id": pr_benefits_id_9,
                "product_id": prs_id_3,
                "icon": "products/benefits/"
                + "3f13e9d47e5d1cf773841f609edcf66dff9cb2e2.svg",
                "name": "Jaminan Uang Pertanggungan Menyeluruh",
                "benefit": "<div>Ahli Waris akan mendapat 100"
                + "% uang pertanggungan jika yang tertanggung tutup usia"
                + " karena kecelakaan</div>",
            },
            {
                "id": pr_benefits_id_10,
                "product_id": prs_id_3,
                "icon": "products/benefits/"
                + "25132ae6a4f4982b3cf2894e126c55620e239246.svg",
                "name": "Perlindungan Biaya Medis Karena Kecelakaan",
                "benefit": "<div>Asuransi dengan penggantian biaya medis"
                + " dari rumah sakit sesuai dengan limit tahunan plan yang"
                + " sudah ditentukan</div>",
            },
            {
                "id": pr_benefits_id_11,
                "product_id": prs_id_3,
                "icon": "products/benefits/"
                + "601864a56db5e057e9ecf9964b5e0d0a049d5e46.svg",
                "name": "Perlindungan Optimal Cacat Total dan Tetap",
                "benefit": "<div>Tertanggung akan mendapat 100%"
                + " uang pertanggungan jika terjadi kecelakaan serta mengalami"
                + " cacat total dan tetap</div>",
            },
            {
                "id": pr_benefits_id_12,
                "product_id": prs_id_4,
                "icon": "products/benefits/"
                + "61780656f966b639da2581aa67bd5882f7c75fa7.svg",
                "name": "Asuransi Kesehatan Super Terjangkau",
                "benefit": "<div>Dapatkan manfaat perlindungan kesehatan"
                + " dengan premi asuransi&nbsp;<br>super terjangkau</div>",
            },
            {
                "id": pr_benefits_id_13,
                "product_id": prs_id_4,
                "icon": "products/benefits/"
                + "daa0c3a6e9741a788f5fdac87260a4a2a27ba040.svg",
                "name": "Jaminan Uang Pertanggungan Menyeluruh",
                "benefit": "<div>100% uang pertanggungan jika"
                + " yang tertanggung tutup usia dalam masa asuransi</div>",
            },
            {
                "id": pr_benefits_id_14,
                "product_id": prs_id_4,
                "icon": "products/benefits/"
                + "6d519522e2d93939cd8353bcda23d6e76fb5c096.svg",
                "name": "Perlindungan Optimal Rawat Inap",
                "benefit": "<div>Santunan tunai harian untuk rawat"
                + " inap Rumah Sakit dan rawat inap ICU</div>",
            }
        ])

    pr_details_id_1 = generate_uuid()
    pr_details_id_2 = generate_uuid()
    pr_details_id_3 = generate_uuid()
    pr_details_id_4 = generate_uuid()
    pr_details_id_5 = generate_uuid()
    pr_details_id_6 = generate_uuid()
    op.bulk_insert(
        pr_details,
        [
            {
                "id": pr_details_id_1,
                "summary": "Asuransi jiwa yang memberikan kamu manfaat"
                + " perlindungan finansial untuk diri sendiri dan orang-orang"
                + " terdekat dari hal tak terduga",
                "description": "<div>Asuransi jiwa yang memberikan"
                + " kamu manfaat perlindungan finansial untuk diri sendiri dan"
                + " orang-orang terdekat dari hal tak terduga</div>",
                "icon": "products/"
                + "c8ab8a5ebb762b440a6db7b830e102a30a22d11f.svg",
                "coverage_period": 1,
                "basic_id": prs_id_1,
                "rider_id": "",
            },
            {
                "id": pr_details_id_2,
                "summary": "Asuransi yang menyiapkan diri kamu dengan"
                + " manfaat perlindungan dari penyakit kritis <br> <br>",
                "description": "<div>Asuransi yang menyiapkan diri"
                + " kamu dengan manfaat perlindungan dari penyakit kritis"
                + "</div>",
                "icon": "products/"
                + "2ba2d0e4226123189a55c80443b731efc13edf54.svg",
                "coverage_period": 1,
                "basic_id": prs_id_2,
                "rider_id": "",
            },
            {
                "id": pr_details_id_3,
                "summary": "Asuransi yang menjaga kamu sepenuhnya dengan"
                + " memberikan perlindungan menyeluruh dari risiko cedera yang"
                + " disebabkan oleh kecelakaan",
                "description": "<div>Asuransi yang menjaga kamu"
                + " sepenuhnya dengan memberikan perlindungan menyeluruh dari"
                + " risiko cedera yang disebabkan oleh kecelakaan</div>",
                "icon": "products/"
                + "4abf9e867e26aa7d0993c747ba5416874c668178.svg",
                "coverage_period": 1,
                "basic_id": prs_id_3,
                "rider_id": "",
            },
            {
                "id": pr_details_id_4,
                "summary": "Maksimalkan perlindungan super kamu dengan manfaat"
                + " dobel untuk risiko kecelakaan ketika berkendara dengan"
                + " motor",
                "description": "<div>Maksimalkan perlindungan super kamu"
                + " dengan manfaat dobel untuk risiko kecelakaan ketika"
                + " berkendara dengan motor</div>",
                "icon": "products/"
                + "s8mvMf8D51v7s4StFjW4fVpr8rJuZExBQxgHPZn9.svg",
                "coverage_period": 1,
                "basic_id": "",
                "rider_id": pr_riders_id_1,
            },
            {
                "id": pr_details_id_5,
                "summary": "Lengkapi perlindungan super kamu dengan manfaat"
                + " dobel untuk risiko kecelakaan khusus setiap hari libur"
                + " nasional",
                "description": "<div>Lengkapi perlindungan super kamu"
                + " dengan manfaat dobel untuk risiko kecelakaan khusus setiap"
                + " hari libur nasional</div>",
                "icon": "",
                "coverage_period": 1,
                "basic_id": "",
                "rider_id": pr_riders_id_2,
            },
            {
                "id": pr_details_id_6,
                "summary": "Produk unggulan yang meringankan beban biaya"
                + " perawatan Rumah Sakit, baik rawat inap maupun ICU.",
                "description": "<div>Produk unggulan yang meringankan"
                + " beban biaya perawatan Rumah Sakit, baik rawat inap maupun"
                + " ICU.</div>",
                "icon": "products/"
                + "27c6a2dcca47393dda84f3d038dd3d115d798520.svg",
                "coverage_period": 1,
                "basic_id": prs_id_4,
                "rider_id": "",
            }
        ])
    pass


def downgrade():
    op.drop_table('products'),
    op.drop_table('product_categories'),
    op.drop_table('product_insurance_types'),
    op.drop_table('product_details'),
    op.drop_table('product_benefits'),
    op.drop_table('product_riders'),
    op.drop_table('product_plans')
    pass
