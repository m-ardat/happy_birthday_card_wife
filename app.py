# ИМПОРТ БИБЛИОТЕК
import streamlit as st
import streamlit_antd_components as sac
from streamlit_extras.let_it_rain import rain

# КОНФИГУРАЦИЯ ПРИЛОЖЕНИЯ
st.set_page_config(
    page_title="Happy Birthday Card",
    page_icon=":material/featured_seasonal_and_gifts:",
    layout="centered",
    menu_items=None
)

# ОФОРМЛЕНИЕ
st.markdown(
    """
    <style>    
    /* НАСТРОЙКИ ШРИФТА */
    /* Изменение цвета текста и шрифта в label */
    [data-testid="stWidgetLabel"] {
        font-size: 14px;                        /* Размер текста */
        font-family: 'Helvetica', sans-serif;   /* Шрифт текста */
    }

    /* Изменение шрифта */
    bodybody, h1, h2, h3, h4, h5, h6, p, div, span, li, a, blockquote, pre, code {
        font-family: 'Helvetica', sans-serif;
    }
    .st-emotion-cache-16tyu1 h1, 
    .st-emotion-cache-16tyu1 h2, 
    .st-emotion-cache-16tyu1 h3, 
    .st-emotion-cache-16tyu1 h4, 
    .st-emotion-cache-16tyu1 h5, 
    .st-emotion-cache-16tyu1 h6, 
    .st-emotion-cache-102y9h7 h1, 
    .st-emotion-cache-102y9h7 h2, 
    .st-emotion-cache-102y9h7 h3, 
    .st-emotion-cache-102y9h7 h4, 
    .st-emotion-cache-102y9h7 h5, 
    .st-emotion-cache-102y9h7 h6,
    .st-emotion-cache-16tyu1 td {
        font-family: 'Helvetica', sans-serif;
    }   

    /* Скрыть кнопку увеличение изображения */
    .st-emotion-cache-z56u96 {
        display: none;
    }

    /* Скрыть якорь заголовка */
    .st-emotion-cache-gi0tri {
        display: none !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ФУНКЦИИ
#Функция дождь шариков
def rain_ballon():
    rain(
        emoji="🎈",
        font_size=46,
        falling_speed=45,
        animation_length="infinite",
    )

def read_txt_file(filepath, encoding='utf-8'):
    with open(filepath, 'r', encoding=encoding) as file:
            return file.read()
# ФРОНТ
# Заголовок
st.markdown("""
<h1 style="text-align: center; 
           margin: -81px 0 15px 0;   /* top, right, bottom, left */
           color: #2e2e2e; 
           font-family: 'Helvetica'; 
           font-size: 4rem;
           font-weight: bold;">
    С Днём Рождения! 🎉
</h1>
""", unsafe_allow_html=True)

# Падающие шарики
rain_ballon()

# Разделение страницы
col1, col2 = st.columns([14, 86], border=False)
with col1:
    # Выбор шага
    step = sac.steps(
        items=[
            sac.StepsItem(title='❤️'),
            sac.StepsItem(title='🌋'),
            sac.StepsItem(title='🚀'),
        ],
        color="#4285b4",
        placement="vertical",
        direction="vertical"
    )

if step == '❤️':
    content_txt = read_txt_file("file_txt/family.txt")
    content_p = "file_photo/p1.jpg"
elif step == '🌋':
    content_txt = read_txt_file("file_txt/trip.txt")
    content_p = "file_photo/p2.jpg"
else:
    content_txt = read_txt_file("file_txt/f.txt")
    content_p = "file_photo/p3.jpg"

with col2:
    col21, col22 = st.columns([1,1], border=False)
    with col21:
        st.image(image=content_p, width=320)
    with col22:
        st.markdown(f"""
        <div style="margin: -20; padding: 0; display: block;">
            <div 
                style="background-color: #FFFAFA; 
                padding: 20px; 
                border-radius: 8px; 
                text-align: left; 
                font-style: italic; 
                color: #2E2E2E;
                white-space: pre-line;
                vertical-align: top;
                margin: 0;">
                {content_txt.strip()}
            </div>
        </div>
        """,
        unsafe_allow_html=True
        )
