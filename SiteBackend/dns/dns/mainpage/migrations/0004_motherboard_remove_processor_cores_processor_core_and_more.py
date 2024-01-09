# Generated by Django 5.0.1 on 2024-01-09 08:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_remove_user_otp1_remove_user_phoneno1_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('image', models.ImageField(upload_to='component_images/', verbose_name='Изображение')),
                ('series', models.CharField(max_length=50, verbose_name='Серия')),
                ('release_year', models.IntegerField(verbose_name='Год релиза')),
                ('form_factor', models.CharField(max_length=50, verbose_name='Форм-фактор')),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Высота')),
                ('width', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Ширина')),
                ('socket', models.CharField(max_length=20, verbose_name='Сокет')),
                ('intel_chipset', models.CharField(max_length=50, verbose_name='Чипсет Intel')),
                ('compatible_intel_processor_cores', models.CharField(max_length=50, verbose_name='Совместимые ядра процессора Intel')),
                ('supported_memory_type', models.CharField(max_length=50, verbose_name='Тип поддерживаемой памяти')),
                ('supported_memory_form_factor', models.CharField(max_length=50, verbose_name='Форм-фактор поддерживаемой памяти')),
                ('num_memory_slots', models.IntegerField(verbose_name='Количество слотов для памяти')),
                ('num_memory_channels', models.IntegerField(verbose_name='Количество каналов памяти')),
                ('max_memory_capacity', models.CharField(max_length=50, verbose_name='Максимальный объем памяти')),
                ('max_memory_frequency', models.CharField(max_length=50, verbose_name='Максимальная частота памяти (JEDEC / без разгона)')),
                ('overclocked_ram_frequency', models.CharField(max_length=50, verbose_name='Частота ОЗУ в разгоне')),
                ('pci_express_version', models.CharField(max_length=50, verbose_name='Версия PCI Express')),
                ('num_pci_express_x16_slots', models.IntegerField(verbose_name='Количество слотов PCI-E x16')),
                ('sli_crossfire_support', models.BooleanField(verbose_name='Поддержка SLI/CrossFire')),
                ('num_cards_in_sli_crossfire', models.IntegerField(verbose_name='Количество карт в режиме SLI/CrossFire')),
                ('num_pci_express_slots', models.IntegerField(verbose_name='Количество слотов PCI-E')),
                ('nvme_support', models.BooleanField(verbose_name='Поддержка NVMe')),
                ('pci_express_drive_version', models.CharField(max_length=50, verbose_name='Версия дисков PCI Express')),
                ('num_m2_connectors', models.IntegerField(verbose_name='Количество разъемов M.2')),
                ('num_sata_ports', models.IntegerField(verbose_name='Количество портов SATA')),
                ('num_usb_back_panel', models.CharField(max_length=50, verbose_name='Количество и тип USB на задней панели')),
                ('video_outputs', models.CharField(max_length=50, verbose_name='Выходы видео')),
                ('num_network_ports_rj45', models.IntegerField(verbose_name='Количество сетевых портов (RJ-45)')),
                ('num_analog_audio_jacks', models.IntegerField(verbose_name='Количество аналоговых аудиоразъемов')),
                ('digital_audio_ports_spdif', models.BooleanField(verbose_name='Цифровые аудиоразъемы (S/PDIF)')),
                ('toslink_spdif_optical', models.BooleanField(verbose_name='TOSLINK (S/PDIF Optical)')),
                ('ps2_ports', models.IntegerField(verbose_name='Порты PS/2')),
                ('internal_usb_type_a_connectors', models.CharField(max_length=50, verbose_name='Внутренние разъемы USB Type-A')),
                ('internal_usb_type_c_connectors', models.CharField(max_length=50, verbose_name='Внутренние разъемы USB Type-C')),
                ('processor_cooling_power_connectors', models.CharField(max_length=50, verbose_name='Разъемы питания системы охлаждения процессора')),
                ('water_pump_connectors', models.CharField(max_length=50, verbose_name='Разъемы для насоса водяного охлаждения (4 pin)')),
                ('case_fans_4_pin_connectors', models.CharField(max_length=50, verbose_name='Разъемы для вентиляторов корпуса (4 pin)')),
                ('case_fans_3_pin_connectors', models.CharField(max_length=50, verbose_name='Разъемы для вентиляторов корпуса (3 pin)')),
                ('five_v_d_g_rgb_backlight_connectors_3_pin', models.CharField(max_length=50, verbose_name='Разъемы 5V-D-G для RGB-подсветки (3 pin)')),
                ('twelve_v_g_r_b_rgb_backlight_connectors_4_pin', models.CharField(max_length=50, verbose_name='Разъемы 12V-G-R-B для RGB-подсветки (4 pin)')),
                ('m2_e_connector_for_wireless_communication_modules', models.CharField(max_length=50, verbose_name='Разъем M.2 (E) для беспроводных модулей связи')),
                ('rs_232_connector_com', models.BooleanField(verbose_name='Разъем RS-232 (COM)')),
                ('lpt_interface', models.BooleanField(verbose_name='Интерфейс LPT')),
                ('sound_scheme', models.CharField(max_length=50, verbose_name='Звуковая схема')),
                ('audio_adapter_chipset', models.CharField(max_length=50, verbose_name='Чипсет аудиоадаптера')),
                ('network_adapter_speed', models.CharField(max_length=50, verbose_name='Скорость сетевого адаптера')),
                ('network_adapter', models.CharField(max_length=50, verbose_name='Сетевой адаптер')),
                ('wifi_standard', models.CharField(max_length=50, verbose_name='Стандарт Wi-Fi')),
                ('bluetooth_version', models.CharField(max_length=50, verbose_name='Версия Bluetooth')),
                ('wireless_adapter', models.CharField(max_length=50, verbose_name='Беспроводной адаптер')),
                ('main_power_connector', models.CharField(max_length=50, verbose_name='Основной разъем питания')),
                ('processor_power_connector', models.CharField(max_length=50, verbose_name='Разъем питания процессора')),
                ('num_power_phases', models.IntegerField(verbose_name='Количество фаз питания')),
                ('passive_cooling', models.BooleanField(verbose_name='Пассивное охлаждение')),
                ('active_cooling', models.BooleanField(verbose_name='Активное охлаждение')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='processor',
            name='cores',
        ),
        migrations.AddField(
            model_name='processor',
            name='core',
            field=models.CharField(default='', max_length=20, verbose_name='Ядро'),
        ),
        migrations.AddField(
            model_name='processor',
            name='heat_release',
            field=models.CharField(default='', max_length=20, verbose_name='Тепловыделение'),
        ),
        migrations.AddField(
            model_name='processor',
            name='l2_cache_size',
            field=models.CharField(default='', max_length=20, verbose_name='Размер кэша L2'),
        ),
        migrations.AddField(
            model_name='processor',
            name='l3_cache_size',
            field=models.CharField(default='', max_length=20, verbose_name='Размер кэша L3'),
        ),
        migrations.AddField(
            model_name='processor',
            name='max_clock_speed',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Максимальная тактовая частота'),
        ),
        migrations.AddField(
            model_name='processor',
            name='max_ram',
            field=models.CharField(default='', max_length=20, verbose_name='Максимальный объем ОЗУ'),
        ),
        migrations.AddField(
            model_name='processor',
            name='max_temperature',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Максимальная температура процессора'),
        ),
        migrations.AddField(
            model_name='processor',
            name='num_channels',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество каналов памяти'),
        ),
        migrations.AddField(
            model_name='processor',
            name='number_cores',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество ядер'),
        ),
        migrations.AddField(
            model_name='processor',
            name='ram_type',
            field=models.CharField(default='', max_length=20, verbose_name='Тип ОЗУ'),
        ),
        migrations.AddField(
            model_name='processor',
            name='release_year',
            field=models.IntegerField(default=2012, validators=[django.core.validators.MinValueValidator(1900)], verbose_name='Год релиза'),
        ),
        migrations.AddField(
            model_name='processor',
            name='technical_process',
            field=models.CharField(default='', max_length=20, verbose_name='Техпроцесс'),
        ),
        migrations.AddField(
            model_name='processor',
            name='threads',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество потоков'),
        ),
        migrations.AddField(
            model_name='processor',
            name='virtualization',
            field=models.BooleanField(default=False, verbose_name='Виртуализация'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='additional_power_connectors',
            field=models.CharField(default='', max_length=50, verbose_name='Дополнительные разъемы питания'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='alu',
            field=models.IntegerField(default=0, verbose_name='Число арифметико-логических блоков'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='connection_connector_form_factor',
            field=models.CharField(default='', max_length=50, verbose_name='Форм-фактор коннектора подключения'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='connection_interface',
            field=models.CharField(default='', max_length=50, verbose_name='Интерфейс подключения'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='cooling_type',
            field=models.CharField(default='', max_length=50, verbose_name='Тип охлаждения'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='designed_for_mining',
            field=models.BooleanField(default=False, verbose_name='Предназначена для майнинга'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='displayport_version',
            field=models.CharField(default='', max_length=10, verbose_name='Версия DisplayPort'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='effective_memory_frequency',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Эффективная частота памяти'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='graphics_card_thickness',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Толщина видеокарты'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='graphics_processor',
            field=models.CharField(default='', max_length=50, verbose_name='Графический процессор'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='hdmi_version',
            field=models.CharField(default='', max_length=10, verbose_name='Версия HDMI'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='max_memory_bandwidth',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Максимальная пропускная способность памяти'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='max_resolution',
            field=models.CharField(default='', max_length=20, verbose_name='Максимальное разрешение'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='memory_bus_bit_depth',
            field=models.IntegerField(default=0, verbose_name='Битовая глубина шины памяти'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='memory_type',
            field=models.CharField(default='', max_length=50, verbose_name='Тип памяти'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='microarchitecture',
            field=models.CharField(default='', max_length=50, verbose_name='Микроархитектура'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='num_fans_installed',
            field=models.IntegerField(default=0, verbose_name='Количество установленных вентиляторов'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='num_monitors_connected',
            field=models.IntegerField(default=0, verbose_name='Количество подключенных мониторов одновременно'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='num_pci_express_lines',
            field=models.IntegerField(default=0, verbose_name='Количество линий PCI Express'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='num_rasterization_blocks',
            field=models.IntegerField(default=0, verbose_name='Количество блоков растеризации'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='num_texture_blocks',
            field=models.IntegerField(default=0, verbose_name='Количество блоков текстурирования'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='power_consumption',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Потребление энергии'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='ray_tracing_support',
            field=models.BooleanField(default=False, verbose_name='Поддержка трассировки лучей'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='recommended_power_supply',
            field=models.CharField(default='', max_length=50, verbose_name='Рекомендуемая мощность блока питания'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='rgb_backlight_synchronization',
            field=models.BooleanField(default=False, verbose_name='Синхронизация RGB-подсветки'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='rt_cores',
            field=models.IntegerField(default=0, verbose_name='Аппаратное ускорение трассировки лучей (RT cores)'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='standard_clock_speed',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Стандартная тактовая частота видеочипа'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='technical_process',
            field=models.CharField(default='', max_length=50, verbose_name='Технический процесс'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='tensor_kernels',
            field=models.IntegerField(default=0, verbose_name='Тензорные ядра'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='turbo_clock_speed',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Турбо-тактовая частота'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='video_card_element_highlighting',
            field=models.BooleanField(default=False, verbose_name='Подсветка элементов видеокарты'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='video_card_length',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Длина видеокарты'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='video_card_width',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Ширина видеокарты'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='video_connectors',
            field=models.CharField(default='', max_length=100, verbose_name='Тип и количество видеоразъемов'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='video_memory_size',
            field=models.IntegerField(default=0, help_text='в гигабайтах', verbose_name='Объем видеопамяти'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Масса'),
        ),
        migrations.AlterField(
            model_name='processor',
            name='clock_speed',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Тактовая частота'),
        ),
        migrations.AlterField(
            model_name='processor',
            name='socket',
            field=models.CharField(default='', max_length=20, verbose_name='Сокет'),
        ),
        migrations.AlterField(
            model_name='videocard',
            name='chipset',
            field=models.CharField(default='', max_length=50, verbose_name='Чипсет'),
        ),
        migrations.AlterField(
            model_name='videocard',
            name='memory_size',
            field=models.IntegerField(default=0, help_text='в гигабайтах', verbose_name='Объем памяти'),
        ),
    ]