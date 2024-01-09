from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class User(AbstractUser):
    phone = models.CharField('Номер телефона', max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

# Добавим related_name для связей с группами и правами
User._meta.get_field('groups').remote_field.related_name = 'mainpage_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'mainpage_user_user_permissions'

class Component(models.Model):
    name = models.CharField('Название', max_length=255)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    quantity = models.IntegerField('Количество')
    image = models.ImageField('Изображение', upload_to='component_images/')

    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name
    
class VideoCard(Component):
    memory_size = models.IntegerField('Объем памяти', help_text='в гигабайтах', default=0)
    designed_for_mining = models.BooleanField('Предназначена для майнинга', default=False)
    graphics_processor = models.CharField('Графический процессор', max_length=50, default='')
    microarchitecture = models.CharField('Микроархитектура', max_length=50, default='')
    technical_process = models.CharField('Технический процесс', max_length=50, default='')
    standard_clock_speed = models.DecimalField('Стандартная тактовая частота видеочипа', max_digits=20, decimal_places=2, default=0.0)
    turbo_clock_speed = models.DecimalField('Турбо-тактовая частота', max_digits=20, decimal_places=2, default=0.0)
    alu = models.IntegerField('Число арифметико-логических блоков', default=0)
    num_texture_blocks = models.IntegerField('Количество блоков текстурирования', default=0)
    num_rasterization_blocks = models.IntegerField('Количество блоков растеризации', default=0)
    ray_tracing_support = models.BooleanField('Поддержка трассировки лучей', default=False)
    rt_cores = models.IntegerField('Аппаратное ускорение трассировки лучей (RT cores)', default=0)
    tensor_kernels = models.IntegerField('Тензорные ядра', default=0)
    video_memory_size = models.IntegerField('Объем видеопамяти', help_text='в гигабайтах', default=0)
    memory_type = models.CharField('Тип памяти', max_length=50, default='')
    memory_bus_bit_depth = models.IntegerField('Битовая глубина шины памяти', default=0)
    max_memory_bandwidth = models.DecimalField('Максимальная пропускная способность памяти', max_digits=10, decimal_places=2, default=0.0)
    effective_memory_frequency = models.DecimalField('Эффективная частота памяти', max_digits=10, decimal_places=2, default=0.0)
    video_connectors = models.CharField('Тип и количество видеоразъемов', max_length=100, default='')
    hdmi_version = models.CharField('Версия HDMI', max_length=10, default='')
    displayport_version = models.CharField('Версия DisplayPort', max_length=10, default='')
    num_monitors_connected = models.IntegerField('Количество подключенных мониторов одновременно', default=0)
    max_resolution = models.CharField('Максимальное разрешение', max_length=20, default='')
    connection_interface = models.CharField('Интерфейс подключения', max_length=50, default='')
    connection_connector_form_factor = models.CharField('Форм-фактор коннектора подключения', max_length=50, default='')
    num_pci_express_lines = models.IntegerField('Количество линий PCI Express', default=0)
    additional_power_connectors = models.CharField('Дополнительные разъемы питания', max_length=50, default='')
    recommended_power_supply = models.CharField('Рекомендуемая мощность блока питания', max_length=50, default='')
    power_consumption = models.DecimalField('Потребление энергии', max_digits=5, decimal_places=2, default=0.0)
    cooling_type = models.CharField('Тип охлаждения', max_length=50, default='')
    num_fans_installed = models.IntegerField('Количество установленных вентиляторов', default=0)
    video_card_element_highlighting = models.BooleanField('Подсветка элементов видеокарты', default=False)
    rgb_backlight_synchronization = models.BooleanField('Синхронизация RGB-подсветки', default=False)
    video_card_length = models.DecimalField('Длина видеокарты', max_digits=5, decimal_places=2, default=0.0)
    video_card_width = models.DecimalField('Ширина видеокарты', max_digits=5, decimal_places=2, default=0.0)
    graphics_card_thickness = models.DecimalField('Толщина видеокарты', max_digits=5, decimal_places=2, default=0.0)
    weight = models.DecimalField('Масса', max_digits=5, decimal_places=2, default=0.0)

class Processor(Component):
    socket = models.CharField('Сокет', max_length=20, default='')
    release_year = models.IntegerField('Год релиза', validators=[MinValueValidator(1900)], default=2012)
    number_cores = models.IntegerField('Количество ядер', validators=[MinValueValidator(1)], default=1)
    threads = models.IntegerField('Количество потоков', validators=[MinValueValidator(1)], default=1)
    l2_cache_size = models.CharField('Размер кэша L2', max_length=20, default='')
    l3_cache_size = models.CharField('Размер кэша L3', max_length=20, default='')
    technical_process = models.CharField('Техпроцесс', max_length=20, default='')
    core = models.CharField('Ядро', max_length=20, default='')
    clock_speed = models.DecimalField('Тактовая частота', max_digits=5, decimal_places=2, default=0.0)
    max_clock_speed = models.DecimalField('Максимальная тактовая частота', max_digits=5, decimal_places=2, default=0.0)
    ram_type = models.CharField('Тип ОЗУ', max_length=20, default='')
    max_ram = models.CharField('Максимальный объем ОЗУ', max_length=20, default='')
    num_channels = models.IntegerField('Количество каналов памяти', validators=[MinValueValidator(1)], default=1)
    heat_release = models.CharField('Тепловыделение', max_length=20, default='')
    max_temperature = models.DecimalField('Максимальная температура процессора', max_digits=5, decimal_places=2, default=0.0)
    virtualization = models.BooleanField('Виртуализация', default=False)

class Motherboard(Component):
    series = models.CharField('Серия', max_length=50)
    release_year = models.IntegerField('Год релиза')
    form_factor = models.CharField('Форм-фактор', max_length=50)
    height = models.DecimalField('Высота', max_digits=5, decimal_places=2)
    width = models.DecimalField('Ширина', max_digits=5, decimal_places=2)
    socket = models.CharField('Сокет', max_length=20)
    intel_chipset = models.CharField('Чипсет Intel', max_length=50)
    compatible_intel_processor_cores = models.CharField('Совместимые ядра процессора Intel', max_length=50)
    supported_memory_type = models.CharField('Тип поддерживаемой памяти', max_length=50)
    supported_memory_form_factor = models.CharField('Форм-фактор поддерживаемой памяти', max_length=50)
    num_memory_slots = models.IntegerField('Количество слотов для памяти')
    num_memory_channels = models.IntegerField('Количество каналов памяти')
    max_memory_capacity = models.CharField('Максимальный объем памяти', max_length=50)
    max_memory_frequency = models.CharField('Максимальная частота памяти (JEDEC / без разгона)', max_length=50)
    overclocked_ram_frequency = models.CharField('Частота ОЗУ в разгоне', max_length=50)
    pci_express_version = models.CharField('Версия PCI Express', max_length=50)
    num_pci_express_x16_slots = models.IntegerField('Количество слотов PCI-E x16')
    sli_crossfire_support = models.BooleanField('Поддержка SLI/CrossFire')
    num_cards_in_sli_crossfire = models.IntegerField('Количество карт в режиме SLI/CrossFire')
    num_pci_express_slots = models.IntegerField('Количество слотов PCI-E')
    nvme_support = models.BooleanField('Поддержка NVMe')
    pci_express_drive_version = models.CharField('Версия дисков PCI Express', max_length=50)
    num_m2_connectors = models.IntegerField('Количество разъемов M.2')
    num_sata_ports = models.IntegerField('Количество портов SATA')
    num_usb_back_panel = models.CharField('Количество и тип USB на задней панели', max_length=50)
    video_outputs = models.CharField('Выходы видео', max_length=50)
    num_network_ports_rj45 = models.IntegerField('Количество сетевых портов (RJ-45)')
    num_analog_audio_jacks = models.IntegerField('Количество аналоговых аудиоразъемов')
    digital_audio_ports_spdif = models.BooleanField('Цифровые аудиоразъемы (S/PDIF)')
    toslink_spdif_optical = models.BooleanField('TOSLINK (S/PDIF Optical)')
    ps2_ports = models.IntegerField('Порты PS/2')
    internal_usb_type_a_connectors = models.CharField('Внутренние разъемы USB Type-A', max_length=50)
    internal_usb_type_c_connectors = models.CharField('Внутренние разъемы USB Type-C', max_length=50)
    processor_cooling_power_connectors = models.CharField('Разъемы питания системы охлаждения процессора', max_length=50)
    water_pump_connectors = models.CharField('Разъемы для насоса водяного охлаждения (4 pin)', max_length=50)
    case_fans_4_pin_connectors = models.CharField('Разъемы для вентиляторов корпуса (4 pin)', max_length=50)
    case_fans_3_pin_connectors = models.CharField('Разъемы для вентиляторов корпуса (3 pin)', max_length=50)
    five_v_d_g_rgb_backlight_connectors_3_pin = models.CharField('Разъемы 5V-D-G для RGB-подсветки (3 pin)', max_length=50)
    twelve_v_g_r_b_rgb_backlight_connectors_4_pin = models.CharField('Разъемы 12V-G-R-B для RGB-подсветки (4 pin)', max_length=50)
    m2_e_connector_for_wireless_communication_modules = models.CharField('Разъем M.2 (E) для беспроводных модулей связи', max_length=50)
    rs_232_connector_com = models.BooleanField('Разъем RS-232 (COM)')
    lpt_interface = models.BooleanField('Интерфейс LPT')
    sound_scheme = models.CharField('Звуковая схема', max_length=50)
    audio_adapter_chipset = models.CharField('Чипсет аудиоадаптера', max_length=50)
    network_adapter_speed = models.CharField('Скорость сетевого адаптера', max_length=50)
    network_adapter = models.CharField('Сетевой адаптер', max_length=50)
    wifi_standard = models.CharField('Стандарт Wi-Fi', max_length=50)
    bluetooth_version = models.CharField('Версия Bluetooth', max_length=50)
    wireless_adapter = models.CharField('Беспроводной адаптер', max_length=50)
    main_power_connector = models.CharField('Основной разъем питания', max_length=50)
    processor_power_connector = models.CharField('Разъем питания процессора', max_length=50)
    num_power_phases = models.IntegerField('Количество фаз питания')
    passive_cooling = models.BooleanField('Пассивное охлаждение')
    active_cooling = models.BooleanField('Активное охлаждение')
