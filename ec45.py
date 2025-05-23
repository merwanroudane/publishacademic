import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Page Configuration ---
st.set_page_config(
	layout="wide",
	page_title="دليلك الشامل للنشر العلمي الدولي",
	page_icon="📚",
	initial_sidebar_state="expanded"
)

# --- Custom CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

    body {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .main > div {
        direction: rtl;
        text-align: right;
    }
    .stApp {
        background-color: #f0f2f6; /* Light gray background */
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Cairo', sans-serif;
        color: #003366; /* Dark Blue */
    }
    h1 {
        text-align: center;
        border-bottom: 3px solid #007bff; /* Primary Blue */
        padding-bottom: 15px;
        margin-bottom: 30px;
    }
    h2 {
        border-right: 5px solid #007bff;
        padding-right: 10px;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    h3 {
        color: #0056b3; /* Medium Blue */
        margin-top: 25px;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        color: white;
    }
    .stExpander {
        border: 1px solid #007bff;
        border-radius: 8px;
        margin-bottom: 15px;
        background-color: #ffffff;
    }
    .stExpander header {
        background-color: #e7f3ff; /* Light Blue */
        color: #003366;
        font-weight: bold;
        font-size: 1.1em;
    }
    .stSelectbox > div > div > div, .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        direction: rtl;
        text-align: right;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-right: 5px solid #17a2b8; /* Teal */
        border-radius: 5px;
        padding: 15px;
        margin: 15px 0;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-right: 5px solid #28a745; /* Green */
        border-radius: 5px;
        padding: 15px;
        margin: 15px 0;
    }
    .warning-box {
        background-color: #fff3cd;
        border: 1px solid #ffeeba;
        border-right: 5px solid #ffc107; /* Yellow */
        border-radius: 5px;
        padding: 15px;
        margin: 15px 0;
    }
    .highlight-box {
        background-color: #e8f4f8;
        padding: 15px;
        border-radius: 5px;
        border-right: 5px solid #3a6ea5;
        margin: 10px 0px;
    }
    .file-example {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        direction: ltr;
        text-align: left;
        border: 1px solid #dee2e6;
        margin-top: 10px;
    }
    .steps-container {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
        border-left: 3px solid #007bff;
    }
    .step {
        margin-bottom: 10px;
        padding-right: 10px;
        position: relative;
    }
    .step-number {
        display: inline-block;
        width: 30px;
        height: 30px;
        background-color: #007bff;
        color: white;
        text-align: center;
        line-height: 30px;
        border-radius: 50%;
        margin-left: 10px;
        font-weight: bold;
    }
    .sidebar .sidebar-content {
        background-color: #003366; /* Dark Blue for sidebar */
        color: #ffffff;
    }
    .sidebar .sidebar-content .stRadio > label > div > p,
    .sidebar .sidebar-content .stSelectbox > label > div > p,
    .sidebar .sidebar-content .stTextInput > label > div > p,
    .sidebar .sidebar-content .stMarkdown p {
        color: #ffffff !important;
    }
    .sidebar .sidebar-content .stRadio > label {
        padding: 8px 10px;
        border-radius: 4px;
    }
    .sidebar .sidebar-content .stRadio > label:hover {
        background-color: #0056b3; /* Medium Blue on hover */
    }
    .sidebar .sidebar-content h2, .sidebar .sidebar-content h3 {
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("📚 دليل النشر العلمي")
st.sidebar.markdown("---")
page = st.sidebar.radio(
	"اختر القسم:",
	[
		"🏠 الصفحة الرئيسية والمقدمة",
		"🔍 المرحلة الأولى: التحضيرات قبل الإرسال",
		"🎯 المرحلة الثانية: اختيار المجلة المناسبة",
		"📂 المرحلة الثالثة: تجهيز ملفات الإرسال",
		"📨 المرحلة الرابعة: عملية الإرسال",
		"⏳ المرحلة الخامسة: ما بعد الإرسال",
		"📊 إحصائيات ومؤشرات النشر",
		"📖 قاموس المصطلحات"
	]
)
st.sidebar.markdown("---")
st.sidebar.info("""
تم تطوير هذا الدليل التفاعلي لمساعدة الباحثين الناطقين بالعربية في فهم خطوات النشر الدولي.
""")

# --- Page Content ---

if page == "🏠 الصفحة الرئيسية والمقدمة":
	st.markdown("<h1>🌍 دليلك الشامل لخطوات ما بعد الكتابة الأكاديمية: النشر الدولي</h1>", unsafe_allow_html=True)
	st.markdown("""
    <p style="text-align: center; font-size: 1.2em; color: #555;">
    مرحباً بك أيها الباحث/الباحثة! بعد أن أتممت كتابة بحثك العلمي، تبدأ رحلة جديدة نحو النشر في مجلة علمية دولية.
    هذا الدليل التفاعلي سيأخذك خطوة بخطوة عبر هذه العملية، مع التركيز على الملفات المطلوبة والنصائح الهامة.
    </p>
    """, unsafe_allow_html=True)

	st.markdown("---")

	col1, col2 = st.columns(2)
	with col1:
		st.markdown("""
        <div class="info-box">
        <h3>🎯 أهداف هذا الدليل</h3>
        <ul>
            <li>شرح خطوات النشر الدولي بالتفصيل.</li>
            <li>توضيح الملفات المطلوبة لكل مرحلة مع أمثلة.</li>
            <li>تقديم نماذج عملية باللغتين العربية والإنجليزية.</li>
            <li>إرشادات لاختيار المجلة المناسبة لبحثك.</li>
            <li>نصائح للتعامل مع عملية المراجعة والرد على المحكمين.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

	with col2:
		st.markdown("""
        <div class="success-box">
        <h3>💡 أهمية النشر الدولي</h3>
        <ul>
            <li>زيادة الاعتراف العلمي والتأثير في مجال بحثك.</li>
            <li>المساهمة في التقدم العلمي العالمي وتبادل المعرفة.</li>
            <li>تعزيز فرص التعاون الدولي مع باحثين آخرين.</li>
            <li>تحسين سيرتك الذاتية الأكاديمية والتطور المهني.</li>
            <li>زيادة فرص الحصول على التمويل البحثي والترقيات.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

	st.markdown("<h2>📈 مراحل عملية النشر الأساسية</h2>", unsafe_allow_html=True)
	stages_data = {
		'المرحلة': [
			'إعداد المخطوطة النهائية ومراجعتها',
			'اختيار المجلة العلمية المناسبة',
			'تجهيز ملفات الإرسال حسب متطلبات المجلة',
			'إرسال البحث عبر نظام المجلة الإلكتروني',
			'المراجعة الأولية من هيئة التحرير',
			'مراجعة الأقران (التحكيم)',
			'استلام قرار المجلة والرد على ملاحظات المحكمين (إذا لزم الأمر)',
			'القبول النهائي ومراجعة النسخة النهائية (Proofs)',
			'النشر الفعلي للبحث (إلكترونياً أو ورقياً)'
		],
		'المدة التقديرية': [
			'أسابيع إلى أشهر (حسب البحث)',
			'أيام إلى أسابيع',
			'أيام إلى أسابيع',
			'ساعات إلى أيام',
			'أيام إلى أسبوعين',
			'أسابيع إلى عدة أشهر',
			'أسابيع إلى أشهر',
			'أيام إلى أسبوعين',
			'فوري (إلكتروني) أو حسب جدول المجلة'
		]
	}
	df_stages = pd.DataFrame(stages_data)
	st.table(df_stages)

	st.subheader("📊 مخطط متوسط المدة الزمنية لمراحل النشر")
	stages_funnel = ['إعداد المخطوط', 'اختيار المجلة', 'الإرسال', 'المراجعة الأولية', 'مراجعة الأقران', 'التعديل',
					 'القبول/الرفض', 'النشر']
	durations_funnel = [30, 7, 2, 7, 60, 21, 3, 14]  # بالأيام (قيم تقديرية)

	fig_funnel = px.funnel(
		x=durations_funnel,
		y=stages_funnel,
		title="متوسط المدة الزمنية التقديرية لكل مرحلة (بالأيام)",
		labels={'x': 'عدد الأيام', 'y': 'المراحل'}
	)
	fig_funnel.update_layout(title_x=0.5, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
	st.plotly_chart(fig_funnel, use_container_width=True)

elif page == "🔍 المرحلة الأولى: التحضيرات قبل الإرسال":
	st.markdown("<h1>🔍 المرحلة الأولى: التحضيرات النهائية قبل الإرسال (Pre-Submission Checks)</h1>",
				unsafe_allow_html=True)
	st.markdown("""
    قبل أن تضغط زر الإرسال، هناك خطوات حاسمة لضمان أن بحثك في أفضل صورة ممكنة ومهيأ للمراجعة.
    """)
	st.markdown("---")

	with st.expander("📝 الخطوة 1: المراجعة النهائية والتدقيق اللغوي (Final Review and Proofreading)"):
		st.markdown("""
        *   **التدقيق اللغوي والنحوي (Grammar and Spell Check):** تأكد من خلو البحث من الأخطاء الإملائية والنحوية. يمكنك الاستعانة بزميل أو خدمة تدقيق لغوي متخصصة، خاصة إذا كانت اللغة الإنجليزية ليست لغتك الأم.
        *   **التماسك والوضوح (Coherence and Clarity):** هل الأفكار متسلسلة ومنطقية؟ هل الحجج واضحة ومدعومة جيداً؟ هل لغة البحث أكاديمية ودقيقة؟
        *   **التنسيق الأولي (Initial Formatting):** راجع متطلبات المجلة بشكل عام (نوع الخط، تباعد الأسطر، حجم الصفحة). بعض المجلات لديها قوالب جاهزة (Templates).
        *   **فحص الانتحال (Plagiarism Check):** استخدم برنامجاً لفحص الانتحال للتأكد من أصالة عملك وتوثيق جميع المصادر بشكل صحيح. (مثل Turnitin, iThenticate). يجب أن تكون نسبة التشابه منخفضة جداً وضمن الحدود المقبولة.
        *   **مراجعة المراجع (References Check):** تأكد من أن جميع المراجع المذكورة في النص موجودة في قائمة المراجع، والعكس صحيح. تأكد من دقة معلومات المراجع (أسماء المؤلفين، سنة النشر، عنوان المقال/الكتاب، اسم المجلة/الناشر).
        """)

	with st.expander("🎯 الخطوة 2: التأكد من ملاءمة المجلة (Ensuring Journal Fit)"):
		st.markdown("""
        إرسال بحثك لمجلة غير مناسبة هو من أكثر الأسباب شيوعاً للرفض المباشر (Desk Rejection).
        *   **نطاق المجلة (Journal Scope):** هل موضوع بحثك يتناسب تماماً مع اهتمامات المجلة وأهدافها؟ اقرأ قسم "Aims and Scope" أو "About the Journal" في موقع المجلة.
        *   **نوعية الأبحاث المنشورة (Types of Published Articles):** هل تنشر المجلة نوع بحثك (بحث أصيل، مراجعة منهجية، دراسة حالة، مقال رأي، إلخ)؟
        *   **الجمهور المستهدف (Target Audience):** هل قراء المجلة هم الجمهور الذي ترغب في الوصول إليه بنتائج بحثك؟
        *   **معامل التأثير (Impact Factor) والترتيب (Quartile Ranking):** هذه مؤشرات لجودة المجلة وتأثيرها، لكن لا تجعلها المعيار الوحيد. الأهم هو الملاءمة.
        *   **اطلع على أعداد حديثة من المجلة:** هل الأبحاث المنشورة مشابهة لبحثك من حيث المنهجية والعمق؟
        """)

	with st.expander("📖 الخطوة 3: قراءة دليل المؤلفين بدقة (Thoroughly Read 'Guide for Authors')"):
		st.markdown("""
        *   **أهم خطوة على الإطلاق!** كل مجلة لها متطلبات خاصة ومفصلة. تجاهل هذه التعليمات قد يؤدي لرفض بحثك مباشرة (Desk Rejection) دون إرساله للمحكمين.
        *   **ابحث عن قسم (Guide for Authors / Instructions for Authors / Submission Guidelines) على موقع المجلة.** هذا القسم هو دستورك عند تجهيز البحث.
        *   **انتبه بشكل خاص إلى:**
            *   **تنسيق المخطوطة (Manuscript Formatting):** الهوامش، نوع وحجم الخط، تباعد الأسطر، طريقة كتابة العناوين الرئيسية والفرعية، ترقيم الصفحات.
            *   **أسلوب كتابة المراجع (Referencing Style):** APA, MLA, Vancouver, Harvard, Chicago, IEEE, إلخ. استخدم برنامج إدارة مراجع (مثل Mendeley, Zotero, EndNote) لتسهيل الأمر وضمان الدقة.
            *   **عدد الكلمات المسموح به (Word Count Limits):** للبحث كاملاً، للملخص، وأحياناً لأقسام معينة.
            *   **متطلبات الملخص (Abstract Requirements):** هل هو ملخص عادي أم مهيكل (Structured Abstract)؟
            *   **متطلبات الأشكال والجداول (Figure and Table Requirements):** الدقة (Resolution - DPI)، الصيغة (TIFF, EPS, JPG, PNG)، طريقة التسمية (Captions)، هل توضع داخل النص أم في نهاية المخطوطة كملفات منفصلة؟
            *   **البيانات المطلوبة (Required Statements/Declarations):**
                *   بيان تضارب المصالح (Conflict of Interest Statement).
                *   بيان مساهمات المؤلفين (Author Contributions).
                *   بيان الموافقة الأخلاقية (Ethical Approval Statement).
                *   بيان توفر البيانات (Data Availability Statement).
                *   بيان التمويل (Funding Statement).
            *   **سياسات المجلة الأخلاقية:** مثل سياسات الانتحال، التعامل مع البيانات، حقوق المشاركين في البحث.
        """)
	st.markdown("---")
	st.success(
		"💡 نصيحة: قم بإنشاء قائمة تحقق (Checklist) بناءً على دليل المؤلفين للمجلة التي اخترتها، وتأكد من استيفاء كل بند قبل الإرسال.")

elif page == "🎯 المرحلة الثانية: اختيار المجلة المناسبة":
	st.markdown("<h1>🎯 المرحلة الثانية: اختيار المجلة المناسبة</h1>", unsafe_allow_html=True)
	st.markdown("""
    <div class='highlight-box'>
    يعد اختيار المجلة المناسبة من أهم الخطوات التي تؤثر على فرص قبول البحث ونشره. يجب مراعاة عدة عوامل عند اختيار المجلة التي تناسب بحثك.
    </div>
    """, unsafe_allow_html=True)

	st.subheader("📋 معايير اختيار المجلة")
	criteria_col1, criteria_col2 = st.columns(2)
	with criteria_col1:
		st.markdown("""
        - <span class='term'>**التخصص والنطاق (Scope):**</span> تأكد من أن موضوع بحثك يتوافق تماماً مع اهتمامات المجلة وأهدافها (Aims and Scope).
        - <span class='term'>**معامل التأثير (Impact Factor - IF):**</span> مؤشر لأهمية المجلة وانتشارها، يعكس متوسط عدد الاستشهادات لمقالاتها.
        - <span class='term'>**التصنيف الربعي (Quartile Ranking - Q1, Q2, Q3, Q4):**</span> يشير إلى مستوى المجلة ضمن تخصصها بناءً على معامل التأثير أو مؤشرات أخرى.
        - <span class='term'>**مدة المراجعة والنشر (Review and Publication Time):**</span> الوقت المتوقع لإتمام عملية التحكيم والنشر. بعض المجلات تذكر متوسط الوقت على موقعها.
        """, unsafe_allow_html=True)
	with criteria_col2:
		st.markdown("""
        - <span class='term'>**رسوم النشر (Article Processing Charges - APC):**</span> التكلفة المالية للنشر، خاصة في مجلات الوصول المفتوح.
        - <span class='term'>**نوع الوصول (Access Type):**</span> هل هي مجلة اشتراك (Subscription)، وصول مفتوح (Open Access)، أم هجينة (Hybrid)؟
        - <span class='term'>**معدل القبول (Acceptance Rate):**</span> نسبة الأبحاث المقبولة من إجمالي الأبحاث المقدمة (قد لا تفصح كل المجلات عن هذا).
        - <span class='term'>**الفهرسة (Indexing):**</span> قواعد البيانات التي تُفهرس فيها المجلة (e.g., Scopus, Web of Science, PubMed, Medline, ERIC).
        """, unsafe_allow_html=True)

	st.subheader("🛠️ أدوات مساعدة لاختيار المجلة")
	st.markdown("""
    هناك العديد من الأدوات عبر الإنترنت التي يمكن أن تساعدك في العثور على المجلات المناسبة لبحثك بناءً على عنوانه وملخصه وكلماته المفتاحية:
    """)
	tools_col1, tools_col2 = st.columns(2)
	with tools_col1:
		st.markdown("""
        - **JournalFinder (Elsevier):** [finder.elsevier.com](https://finder.elsevier.com)
        - **Journal Suggester (Springer Nature):** [journalsuggester.springer.com](https://journalsuggester.springer.com)
        - **Wiley Journal Finder:** [journalfinder.wiley.com](https://journalfinder.wiley.com)
        - **Taylor & Francis Journal Suggester:** [authorservices.taylorandfrancis.com/journal-suggester/](https://authorservices.taylorandfrancis.com/journal-suggester/)
        """)
	with tools_col2:
		st.markdown("""
        - **JANE (Journal/Author Name Estimator):** [jane.biosemantics.org](http://jane.biosemantics.org/) (خاصة للمجالات الطبية الحيوية)
        - **Web of Science Master Journal List:** [mjl.clarivate.com](https://mjl.clarivate.com/home) (للبحث عن المجلات المفهرسة في WoS)
        - **Scopus Sources:** [scopus.com/sources](https://www.scopus.com/sources.uri) (للبحث عن المجلات المفهرسة في Scopus)
        - **Directory of Open Access Journals (DOAJ):** [doaj.org](https://doaj.org/) (للبحث عن مجلات الوصول المفتوح الموثوقة)
        """)

	st.subheader("💡 استراتيجية الاختيار السليم")
	st.markdown("""
    <div class='steps-container'>
        <div class='step'><span class='step-number'>1</span> حدد قائمة أولية من 5-10 مجلات محتملة بناءً على نطاقها وملاءمتها لبحثك.</div>
        <div class='step'><span class='step-number'>2</span> راجع الأبحاث المنشورة مؤخرًا في هذه المجلات للتأكد من توافق نوعية ومستوى الأبحاث مع بحثك.</div>
        <div class='step'><span class='step-number'>3</span> افحص معايير كل مجلة (معامل التأثير، التصنيف، مدة المراجعة، رسوم النشر، الفهرسة).</div>
        <div class='step'><span class='step-number'>4</span> اقرأ دليل المؤلفين (Guide for Authors) للمجلات المختصرة في قائمتك.</div>
        <div class='step'><span class='step-number'>5</span> رتب المجلات حسب الأولوية بناءً على تقييمك وأهدافك من النشر.</div>
        <div class='step'><span class='step-number'>6</span> ابدأ بالتقديم للمجلة الأعلى في قائمتك، ولا تقدم لنفس البحث في أكثر من مجلة في نفس الوقت.</div>
    </div>
    """, unsafe_allow_html=True)

	st.warning("""
    **⚠️ تحذير من المجلات المفترسة (Predatory Journals):**
    - هي مجلات تدعي أنها علمية ومحكمة ولكن هدفها الأساسي هو الربح المادي من رسوم النشر دون تقديم خدمات تحريرية أو تحكيم حقيقي.
    - **علامات تدل عليها:** وعود بالنشر السريع جداً، طلب رسوم نشر مرتفعة بشكل غير مبرر، موقع إلكتروني غير احترافي ومليء بالأخطاء، نطاق المجلة واسع جداً وغير متخصص، هيئة تحرير وهمية أو غير معروفة، صعوبة في التواصل مع المجلة.
    - **كيفية التحقق:** استخدم قائمة Beall (على الرغم من أنها لم تعد محدثة بانتظام، يمكن البحث عن أرشيفاتها)، تحقق من فهرسة المجلة في قواعد بيانات موثوقة (Scopus, WoS, DOAJ, PubMed)، استشر زملاءك ذوي الخبرة.
    """)

elif page == "📂 المرحلة الثالثة: تجهيز ملفات الإرسال":
	st.markdown("<h1>📂 المرحلة الثالثة: تجهيز ملفات الإرسال (Preparing Submission Files)</h1>", unsafe_allow_html=True)
	st.markdown("""
    <div class='info-box'>
    قد تختلف الملفات المطلوبة قليلاً من مجلة لأخرى، ولكن هذه هي الأساسيات. دائماً ارجع إلى "دليل المؤلفين" الخاص بالمجلة للتأكد.
    </div>
    """, unsafe_allow_html=True)

	# Summary table of files (from ec.py idea)
	st.subheader("📋 قائمة مرجعية للملفات الأساسية")
	files_data = [
		{"الملف": "رسالة التغطية (Cover Letter)", "ملاحظات": "مهمة جداً، تقدم بحثك للمحرر."},
		{"الملف": "المخطوطة الرئيسية (Main Manuscript)", "ملاحظات": "قد تكون معماة (Blinded) أو بمعلومات المؤلفين."},
		{"الملف": "صفحة العنوان (Title Page)", "ملاحظات": "غالباً ملف منفصل، يحتوي معلومات المؤلفين الكاملة."},
		{"الملف": "الأشكال (Figures)", "ملاحظات": "ملفات منفصلة، عالية الدقة."},
		{"الملف": "الجداول (Tables)", "ملاحظات": "قد تكون في نهاية المخطوطة أو ملفات منفصلة."},
		{"الملف": "المواد التكميلية (Supplementary Materials)",
		 "ملاحظات": "إن وجدت، مثل مجموعات البيانات، الفيديوهات، إلخ."},
		{"الملف": "بيان مساهمات المؤلفين (Author Contributions)", "ملاحظات": "يوضح دور كل مؤلف."},
		{"الملف": "بيان تضارب المصالح (Conflict of Interest)", "ملاحظات": "إلزامي في معظم المجلات."},
		{"الملف": "بيان الموافقة الأخلاقية (Ethical Approval)", "ملاحظات": "إذا كان البحث يتضمن بشر أو حيوانات."},
		{"الملف": "بيان توفر البيانات (Data Availability)", "ملاحظات": "يزداد الطلب عليه."},
	]
	df_files_checklist = pd.DataFrame(files_data)
	st.table(df_files_checklist)
	st.markdown("---")

	with st.expander("📄 1. رسالة التغطية (Cover Letter)"):
		st.markdown("""
        **الغرض:** رسالة رسمية موجهة لرئيس تحرير المجلة، تقدم فيها بحثك وتوضح أهميته وملاءمته للمجلة. هي فرصتك الأولى لإقناع المحرر بأن بحثك يستحق المراجعة.
        **المحتويات الأساسية:**
        *   معلوماتك ومعلومات المؤلفين المشاركين (Your and co-authors' information).
        *   اسم رئيس التحرير والمجلة (Editor's name and Journal name).
        *   عنوان البحث (Manuscript title).
        *   نوع المقال (e.g., Original Article, Review, Case Report).
        *   بيان موجز عن أهمية البحث، مشكلة البحث، أبرز نتائجه، وما يضيفه للمعرفة في هذا المجال (Brief statement of significance and main findings).
        *   لماذا تعتقد أن بحثك مناسب لهذه المجلة بالذات (Why your manuscript is suitable for this specific journal - اربطه بنطاق المجلة أو أبحاث منشورة فيها).
        *   إقرار بأن البحث أصيل، ولم يُنشر سابقاً، ولم يُقدم للنشر في مجلة أخرى بالتزامن (Declaration of originality and exclusivity).
        *   بيان تضارب المصالح (Conflict of interest statement - أو الإشارة إلى أنه مذكور في ملف منفصل).
        *   تأكيد موافقة جميع المؤلفين على الإرسال.
        *   معلومات الاتصال بالمؤلف المراسل (Corresponding author's contact details).
        *   (اختياري ولكن محبذ) اقتراح محكمين مؤهلين (Optional: Suggest potential qualified reviewers - مع ذكر سبب اقتراحهم والتأكيد على عدم وجود تضارب مصالح معهم).
        *   (اختياري) ذكر أي محكمين تود استبعادهم مع تبرير موجز.
        """)
		st.subheader("مثال مبسط لرسالة التغطية (Simplified Cover Letter Example):")
		tab_ar_cl, tab_en_cl = st.tabs(["📝 نموذج بالعربية (للتوضيح)", "📝 English Template (Typical)"])
		with tab_ar_cl:
			st.code("""
[تاريخ اليوم]

[اسم رئيس التحرير] (إذا كان معروفاً، وإلا "Dear Editor-in-Chief,")
رئيس تحرير مجلة [اسم المجلة]
[عنوان المجلة، إن وجد]

السيد/السيدة رئيس التحرير،

يسرنا أن نقدم مخطوطة بحثنا بعنوان: "[عنوان البحث كاملاً]" للنظر في نشرها في مجلتكم الموقرة، [اسم المجلة]، كـ [نوع المقال: مثلاً، بحث أصيل Original Research Article].

[فقرة موجزة (2-3 جمل) تشرح مشكلة البحث الرئيسية التي يتناولها المقال، والفجوة المعرفية التي يسعى لسدها.]
[فقرة موجزة (2-3 جمل) تلخص المنهجية الرئيسية المستخدمة والنتائج الأكثر أهمية في البحث، وما هي المساهمة الجديدة أو الأهمية الرئيسية لهذه النتائج.]
[جملة أو اثنتين توضحان لماذا هذا البحث مناسب بشكل خاص لهذه المجلة. على سبيل المثال: "نعتقد أن هذا العمل يتوافق تمامًا مع نطاق مجلتكم الذي يركز على [...] ويثري النقاش الحالي حول [...] الذي ظهر في مقالات حديثة منشورة لديكم."]

نؤكد أن هذا البحث هو عمل أصيل لجميع المؤلفين المذكورين، ولم يتم نشره مسبقاً، ولا هو قيد النظر للنشر في أي مجلة أخرى. جميع المؤلفين قد وافقوا على محتوى المخطوطة وعلى إرسالها لهذه المجلة.
نقر بعدم وجود أي تضارب في المصالح يتعلق بهذا البحث. (أو: "تم الكشف عن تضارب المصالح المحتمل في بيان منفصل وفقًا لسياسة المجلة.")

[اختياري: "يسعدنا اقتراح المحكمين التاليين لخبرتهم في هذا المجال، مع التأكيد على عدم وجود أي تضارب مصالح معهم:"]
[1. د. اسم المحكم الأول، انتماؤه، بريده الإلكتروني]
[2. د. اسم المحكم الثاني، انتماؤه، بريده الإلكتروني]

نشكركم على وقتكم واهتمامكم، ونتطلع لسماع ردكم قريباً.

مع خالص التقدير،

[اسمك بالكامل - المؤلف المراسل]
[مؤهلاتك العلمية]
[انتماؤك المؤسسي (الجامعة/المركز البحثي)]
[بريدك الإلكتروني]
[رقم هاتفك (اختياري)]
[قائمة بأسماء جميع المؤلفين وانتماءاتهم إذا لم تكن مدرجة في صفحة العنوان بشكل منفصل أو إذا طلبت المجلة ذلك هنا]
            """, language="text")
		with tab_en_cl:
			st.code("""
[Date]

Dr. [Editor's Full Name] (If known, otherwise "Dear Editor-in-Chief,")
Editor-in-Chief, [Journal Name]
[Journal Address, if applicable]

Dear Dr. [Editor's Last Name],

We are pleased to submit our manuscript entitled, "[Full Manuscript Title]," for consideration for publication in [Journal Name] as an [Article Type, e.g., Original Research Article].

[This paragraph should briefly state the problem your research addresses and the gap in knowledge it aims to fill (2-3 sentences).]
[This paragraph should summarize the main methodology used, the most significant findings of your study, and their primary contribution or importance (2-3 sentences).]
[One or two sentences explaining why this manuscript is particularly suitable for this journal. For example: "We believe this work aligns well with the scope of [Journal Name], which focuses on [...], and will be of interest to your readership as it contributes to the ongoing discussion on [...] highlighted in recent articles in your journal."]

We confirm that this manuscript is original work from all listed authors, has not been published previously, and is not currently under consideration for publication elsewhere. All authors have approved the manuscript and agree with its submission to [Journal Name].
We declare no conflicts of interest related to this research. (Or: "Potential conflicts of interest have been disclosed in a separate statement as per the journal's policy.")

[Optional: "We would be pleased to suggest the following individuals as potential reviewers due to their expertise in this field, and we confirm no conflicts of interest with them:"]
[1. Dr. Reviewer Name One, Affiliation, Email]
[2. Dr. Reviewer Name Two, Affiliation, Email]

Thank you for your time and consideration. We look forward to hearing from you.

Sincerely,

[Your Full Name - Corresponding Author]
[Your Degrees/Credentials]
[Your Affiliation (University/Research Center)]
[Your Email Address]
[Your Phone Number (Optional)]
[List of all co-authors and their affiliations if required here by the journal]
            """, language="text")

	with st.expander("📄 2. المخطوطة الرئيسية (Main Manuscript)"):
		st.markdown("""
        *   **غالباً ما تكون بدون معلومات المؤلفين (Anonymous/Blinded Manuscript for double-blind review):** العديد من المجلات تتبع نظام المراجعة المزدوجة التعمية. في هذه الحالة، يجب إزالة أي معلومات تعريفية من المخطوطة الرئيسية (الأسماء، الانتماءات، الإشارة المباشرة لمشاريع سابقة للمؤلفين، الشكر لمؤسسات معينة قد تكشف الهوية، معلومات في خصائص الملف). تأكد من مراجعة دليل المجلة حول كيفية "تعمية" المخطوطة.
        *   **الهيكل النموذجي (Typical Structure - IMRaD for empirical papers):**
            *   **العنوان (Title):** واضح، موجز، وجاذب، يعكس محتوى البحث بدقة.
            *   **الملخص (Abstract):** موجز شامل للبحث (عادة 150-300 كلمة). يجب أن يتضمن: خلفية/أهداف (Background/Objectives)، طرق (Methods)، نتائج رئيسية (Key Results)، واستنتاجات (Conclusions). بعض المجلات تطلب ملخصاً مهيكلاً (Structured Abstract).
            *   **الكلمات المفتاحية (Keywords):** 3-7 كلمات تساعد في فهرسة البحث وتسهيل العثور عليه. اختر كلمات دقيقة وغير عامة جداً.
            *   **المقدمة (Introduction):** تقدم خلفية المشكلة، أهميتها، مراجعة موجزة لأهم الدراسات السابقة ذات الصلة (لتوضيح الفجوة البحثية)، الفجوة البحثية التي يعالجها بحثك، أهداف البحث وأسئلته أو فرضياته.
            *   **المواد والطرق (Materials and Methods / Methodology):** وصف تفصيلي لكيفية إجراء البحث بما يسمح للباحثين الآخرين بتكرار الدراسة. يشمل: تصميم البحث، مجتمع وعينة الدراسة وكيفية اختيارها، أدوات جمع البيانات وكيفية تطويرها أو اختيارها (مع ذكر مصداقيتها وثباتها إذا كانت أدوات قياس)، إجراءات البحث، وطرق التحليل الإحصائي المستخدمة.
            *   **النتائج (Results):** عرض موضوعي وموجز للنتائج التي تم التوصل إليها، بدون تفسير أو مناقشة. تُستخدم الجداول والأشكال لعرض البيانات بفعالية. يجب أن يكون النص مكملاً للجداول والأشكال وليس تكراراً لها.
            *   **المناقشة (Discussion):** هذا هو قلب البحث. هنا تقوم بتفسير نتائجك، ربطها بأهداف البحث وفرضياته، مقارنتها بنتائج الدراسات السابقة (توضيح أوجه الاتفاق والاختلاف وأسبابها المحتملة)، تحديد نقاط القوة والضعف في دراستك (القيود)، ذكر الآثار النظرية والتطبيقية للنتائج، وتقديم توصيات لأبحاث مستقبلية.
            *   **الاستنتاجات (Conclusion):** خلاصة مركزة لأهم ما توصل إليه البحث وإجابة مباشرة لأسئلة البحث. تجنب تكرار الملخص أو النتائج. يجب أن تكون الاستنتاجات مدعومة بالنتائج المعروضة.
            *   **(اختياري حسب المجلة، قد تكون في ملفات منفصلة أو ضمن أقسام أخرى) الإقرارات (Declarations):**
                *   بيان توفر البيانات (Data Availability Statement)
                *   بيان التمويل (Funding Statement)
                *   بيان مساهمات المؤلفين (Author Contributions)
                *   بيان الموافقة الأخلاقية (Ethical Approval Statement)
                *   بيان تضارب المصالح (Conflict of Interest Statement)
            *   **الشكر والتقدير (Acknowledgements):** شكر للأفراد أو المؤسسات التي قدمت مساعدة فنية، أو دعماً مالياً (إذا لم يكن في بيان التمويل)، أو مراجعة لغوية، إلخ (وليس المؤلفين المساهمين).
            *   **المراجع (References):** قائمة بجميع المصادر التي تم الاستشهاد بها في النص، منسقة بدقة حسب أسلوب المجلة المطلوب (e.g., APA, MLA, Vancouver).
            *   **(اختياري حسب المجلة) الملاحق (Appendices):** تحتوي على مواد تفصيلية لا تناسب النص الرئيسي (مثل استبيان كامل، خوارزميات معقدة).
        *   **الأشكال والجداول:** تأكد من أنها واضحة، مرقمة، ولها عناوين وشروح كافية. يجب الإشارة إليها في النص (e.g., "كما هو موضح في الجدول 1..." أو "... (الشكل 2)").
        """)

	with st.expander("📄 3. صفحة العنوان (Title Page)"):
		st.markdown("""
        **الغرض:** تحتوي على معلومات تعريفية لا تُدرج عادة في المخطوطة الرئيسية إذا كانت المراجعة مزدوجة التعمية. تُرفع كملف منفصل.
        **المحتويات الأساسية (قد تختلف قليلاً):**
        *   **عنوان البحث كاملاً (Full manuscript title).**
        *   **أسماء جميع المؤلفين بالكامل (Full names of all authors)** بالترتيب المتفق عليه، مع ذكر درجاتهم العلمية إذا طلبت المجلة.
        *   **انتماءاتهم المؤسسية (Affiliations):** القسم، الكلية، الجامعة/المؤسسة، المدينة، الدولة لكل مؤلف. استخدم أرقاماً مرتفعة لربط المؤلف بانتمائه إذا كان هناك عدة انتماءات.
        *   **معلومات المؤلف المراسل (Corresponding author):** الاسم، الانتماء الكامل، العنوان البريدي الكامل، البريد الإلكتروني المؤسسي، رقم الهاتف (أحياناً).
        *   **(أحياناً) العنوان المختصر للترويسة (Running head / Short title):** عنوان قصير لا يتجاوز عدد معين من الأحرف يظهر في أعلى صفحات المقال المنشور.
        *   **(أحياناً) عدد الكلمات في المخطوطة، عدد الأشكال، وعدد الجداول.**
        *   **(أحياناً) الكلمات المفتاحية (Keywords).**
        *   **(أحياناً) إقرارات مثل تضارب المصالح أو التمويل إذا طلبت المجلة ذلك في صفحة العنوان.**
        """)
		st.subheader("مثال لصفحة العنوان (Title Page Example):")
		st.markdown("--- **باللغة الإنجليزية (Typical English Version)** ---")
		st.code("""
Title: [Your Full Manuscript Title Here. Make it Specific and Informative]

Authors:
[Author One Full Name]¹, M.Sc.
[Author Two Full Name]², Ph.D.
[Author Three Full Name]¹, M.D.

Affiliations:
¹[Department, Faculty, University/Institution, City, Postal Code, Country - for Author One and Three]
²[Research Center, Institute, City, Postal Code, Country - for Author Two]

Corresponding Author:
Dr. [Corresponding Author's Full Name]
[Full Affiliation: Department, Faculty, University/Institution]
[Full Postal Address, City, Postal Code, Country]
Email: [institutional_email@example.com]
Phone: [+CountryCode AreaCode Number (Optional)]

Running Head: [A Short Title for the Manuscript, e.g., Impact of X on Y] (Max 50 characters, check journal guidelines)

Keywords: [Keyword 1]; [Keyword 2]; [Keyword 3]; [Keyword 4]; [Keyword 5] (Check journal for number and separator)

Word Count:
Abstract: [e.g., 250 words]
Main Text: [e.g., 5000 words]

Number of Figures: [e.g., 3]
Number of Tables: [e.g., 2]

Conflict of Interest Statement: The authors declare no conflicts of interest. (Or state any conflicts)
Funding: This research was funded by [Funding Body], grant number [XXXX]. (Or state no funding)
Author Contributions: (May be required here or as a separate statement)
Ethical Approval: (May be required here or as a separate statement)

        """, language="text")

	with st.expander("🖼️📊 4. الأشكال والجداول (Figures and Tables)"):
		st.markdown("""
        *   **الجودة العالية (High Resolution):** يجب أن تكون الأشكال واضحة وذات دقة عالية (عادة 300 DPI للصور الملونة/تدرج الرمادي، و 600-1200 DPI للرسوم الخطية/النصية).
        *   **الصيغ المقبولة (Accepted Formats):** TIFF, EPS, JPEG (عالي الجودة), PNG هي صيغ شائعة. بعض المجلات تفضل صيغاً معينة (مثل TIFF أو EPS للرسوم البيانية). راجع دليل المؤلفين.
        *   **التسميات والشروح (Captions and Legends):** كل شكل وكل جدول يجب أن يكون له تسمية (caption) مرقمة (e.g., Figure 1, Table 1) وشرح (legend) وافٍ يوضح محتواه بشكل مستقل دون الحاجة للرجوع للنص. الشروح توضع أسفل الأشكال وفوق الجداول عادةً.
        *   **ملفات منفصلة (Separate Files):** غالباً ما تطلب المجلات رفع كل شكل وكل جدول كملف منفصل، أو تجميع الأشكال في ملف واحد والجداول في ملف آخر، أو وضعها في نهاية المخطوطة بعد قائمة المراجع. اتبع تعليمات المجلة بدقة.
        *   **التسمية المنهجية للملفات (Systematic File Naming):** مثلاً Figure1.tiff, Table1.docx, SupplementaryFile1.pdf.
        *   **حجم الخط ونوعه داخل الأشكال:** يجب أن يكون واضحاً ومقروءاً حتى بعد التصغير ليناسب عرض عمود المجلة.
        *   **الألوان:** تأكد من أن الألوان المستخدمة واضحة ومتباينة، وأنها ستكون واضحة أيضاً إذا طُبعت المجلة باللونين الأبيض والأسود (إذا كان ذلك محتملاً).
        *   **الجداول:** يجب أن تُنشأ باستخدام أداة الجداول في برنامج معالجة النصوص (مثل Word) وليس كصور. يجب أن تكون بسيطة ومفهومة.
        """)

	with st.expander("➕ 5. المواد التكميلية (Supplementary Materials / Supporting Information) - إن وجدت"):
		st.markdown("""
        *   **الغرض:** أي مواد تدعم البحث ولكنها ليست ضرورية لفهم النص الرئيسي ولا يمكن إدراجها فيه بسبب الحجم أو النوع (مثل: مجموعات بيانات خام كبيرة، مقاطع فيديو، كود برمجي، استبيانات مفصلة، بروتوكولات تجريبية طويلة، أشكال إضافية).
        *   **التنسيق:** يتم توضيح التنسيق المطلوب في دليل المؤلفين. عادةً ما تُرفع كملفات منفصلة ويتم الإشارة إليها في النص الرئيسي.
        *   **المراجعة:** تخضع المواد التكميلية للمراجعة مع المخطوطة الرئيسية.
        """)

	with st.expander("✍️ 6. بيان مساهمات المؤلفين (Author Contribution Statement)"):
		st.markdown("""
        *   **الغرض:** توضيح دور كل مؤلف في البحث لضمان الشفافية والمسؤولية. العديد من المجلات تتبع تصنيف CRediT (Contributor Roles Taxonomy) أو تطلب وصفاً نصياً لمساهمة كل مؤلف.
        *   **مثال (باستخدام CRediT taxonomy):**
            *   **[اسم المؤلف الأول]:** Conceptualization, Methodology, Software, Validation, Formal Analysis, Investigation, Resources, Data Curation, Writing – Original Draft, Writing – Review & Editing, Visualization, Supervision, Project Administration, Funding Acquisition.
            *   **[اسم المؤلف الثاني]:** Conceptualization, Methodology, Software, Validation, Formal Analysis, Investigation, Resources, Data Curation, Writing – Original Draft, Writing – Review & Editing, Visualization.
            *   **[اسم المؤلف الثالث]:** Supervision, Project Administration, Funding Acquisition.
        *   **بالعربية (للتوضيح باستخدام CRediT):**
            *   **[اسم المؤلف الأول]:** وضع التصور، المنهجية، تطوير البرمجيات، التحقق من الصحة، التحليل الرسمي، التحقيق، توفير الموارد، تنظيم البيانات، كتابة المسودة الأصلية، المراجعة والتحرير، التمثيل البصري، الإشراف، إدارة المشروع، الحصول على التمويل.
            *   **[اسم المؤلف الثاني]:** وضع التصور، المنهجية، تطوير البرمجيات، التحقق من الصحة، التحليل الرسمي، التحقيق، توفير الموارد، تنظيم البيانات، كتابة المسودة الأصلية، المراجعة والتحرير، التمثيل البصري.
            *   **[اسم المؤلف الثالث]:** الإشراف، إدارة المشروع، الحصول على التمويل.
        *   **ملاحظة:** يجب أن يكون جميع المؤلفين قد وافقوا على بيان مساهماتهم.
        """)

	with st.expander("⚖️ 7. بيان تضارب المصالح (Conflict of Interest - COI - Statement)"):
		st.markdown("""
        *   **الغرض:** الإفصاح عن أي علاقات مالية أو شخصية أو ارتباطات أخرى قد يُنظر إليها على أنها تؤثر على موضوعية البحث أو تفسير نتائجه. الشفافية هي المفتاح.
        *   **مثال إذا لا يوجد تضارب (Example if no conflict):** "The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper."
            *   **بالعربية:** "يقر المؤلفون بعدم وجود أي تضارب مصالح مالي أو شخصي معروف يمكن أن يكون له تأثير واضح على العمل المذكور في هذا البحث."
        *   **مثال إذا يوجد تضارب (Example if conflict exists):** "[Author A] has received research grants from [Company X]. [Author B] is a consultant for [Company Y] and holds stock in the company. [Author C] is a member of the advisory board for [Organization Z]."
            *   **بالعربية:** "[المؤلف أ] تلقى منحاً بحثية من [شركة س]. [المؤلف ب] يعمل كمستشار لـ [شركة ص] ويمتلك أسهماً فيها. [المؤلف ج] عضو في المجلس الاستشاري لـ [منظمة ع]."
        *   **ملاحظة:** يجب أن يقدم كل مؤلف بياناً، أو يتم تقديم بيان موحد نيابة عن جميع المؤلفين.
        """)

	with st.expander("📜 8. بيان الموافقة الأخلاقية (Ethical Approval Statement) - إذا كان البحث يتضمن بشر أو حيوانات"):
		st.markdown("""
        *   **الغرض:** تأكيد الحصول على الموافقات اللازمة من لجان الأخلاقيات المختصة (Institutional Review Board - IRB أو Ethics Committee) قبل بدء البحث.
        *   **المحتوى:** يجب أن يذكر اسم اللجنة التي منحت الموافقة، رقم الموافقة (إذا وجد)، وتاريخها. وإذا كان البحث على بشر، يجب ذكر أنه تم الحصول على موافقة مستنيرة (Informed Consent) من المشاركين (أو أولياء أمورهم للقصر).
        *   **مثال (Example):** "This study was conducted in accordance with the Declaration of Helsinki, and the protocol was approved by the Ethics Committee of [Name of Institution/Organization] (Approval No. [XYZ/123], Date: [YYYY-MM-DD]). Informed consent was obtained from all subjects involved in the study."
            *   **بالعربية:** "أجريت هذه الدراسة وفقاً لمبادئ إعلان هلسنكي، وتمت الموافقة على بروتوكول البحث من قبل لجنة أخلاقيات البحث العلمي في [اسم المؤسسة/المنظمة] (رقم الموافقة [XYZ/123]، بتاريخ [YYYY-MM-DD]). تم الحصول على موافقة مستنيرة من جميع المشاركين في الدراسة."
        *   في حالة دراسات الحيوان، يجب ذكر الالتزام بالإرشادات الخاصة برعاية واستخدام حيوانات التجارب.
        """)

	with st.expander("💾 9. بيان توفر البيانات (Data Availability Statement) - يزداد الطلب عليه"):
		st.markdown("""
        *   **الغرض:** توضيح أين وكيف يمكن للباحثين الآخرين الوصول إلى البيانات التي استند إليها البحث، لتعزيز الشفافية وإمكانية تكرار النتائج.
        *   **أمثلة (Examples) - اختر ما يناسب بحثك وسياسة المجلة:**
            *   "The data presented in this study are available on request from the corresponding author. The data are not publicly available due to [state reason, e.g., privacy or ethical restrictions]." (البيانات متاحة عند الطلب من المؤلف المراسل. البيانات ليست متاحة للعامة بسبب [اذكر السبب، مثل قيود الخصوصية أو الأخلاقية])
            *   "The data presented in this study are openly available in [Repository Name, e.g., FigShare, Zenodo, Dryad] at [DOI or URL]." (البيانات متاحة بشكل مفتوح في [اسم المستودع] على الرابط/المعرف [DOI أو URL])
            *   "All data generated or analysed during this study are included in this published article [and its supplementary information files]." (جميع البيانات التي تم إنشاؤها أو تحليلها خلال هذه الدراسة مدرجة في هذا المقال المنشور [وملفاته المعلوماتية التكميلية])
            *   "The data that support the findings of this study are available from [Third party source, e.g., specific database name] but restrictions apply to the availability of these data, which were used under license for the current study, and so are not publicly available. Data are however available from the authors upon reasonable request and with permission of [Third party source]."
            *   "Data sharing not applicable to this article as no datasets were generated or analysed during the current study." (لا ينطبق مشاركة البيانات على هذا المقال حيث لم يتم إنشاء أو تحليل أي مجموعات بيانات خلال الدراسة الحالية - مناسب للمقالات النظرية أو المراجعات التي لا تعتمد على بيانات جديدة).
        """)

elif page == "📨 المرحلة الرابعة: عملية الإرسال":
	st.markdown("<h1>📨 المرحلة الرابعة: عملية الإرسال عبر نظام المجلة (Submission Process)</h1>",
				unsafe_allow_html=True)
	st.markdown("""
    <div class='warning-box'>
    معظم المجلات تستخدم أنظمة إلكترونية لإدارة المخطوطات مثل Editorial Manager, ScholarOne (Manuscript Central), eJournal Press, Open Journal Systems (OJS) وغيرها. الخطوات قد تختلف قليلاً في المظهر والتسميات، ولكن المبدأ العام متشابه.
    </div>
    """, unsafe_allow_html=True)

	with st.expander("🖥️ الخطوات التفصيلية لعملية الإرسال عبر الإنترنت"):
		st.markdown("""
        1.  **الوصول إلى نظام الإرسال:**
            *   اذهب إلى موقع المجلة وابحث عن رابط مثل "Submit Manuscript", "Author Submission", "Submit Your Paper", أو "Author Login".
        2.  **إنشاء حساب أو تسجيل الدخول (Create Account / Login):**
            *   إذا كنت ترسل للمجلة لأول مرة، ستحتاج لإنشاء حساب جديد (Register). قد يُطلب منك معرف ORCID ID (وهو معرف فريد للباحثين، يُنصح بالحصول عليه).
            *   إذا كان لديك حساب بالفعل، قم بتسجيل الدخول.
        3.  **بدء إرسال جديد (Start New Submission / Submit New Manuscript):**
            *   عادة ما يكون هناك خيار لبدء إرسال جديد. قد تحتاج لاختيار نوع المقال (Article Type) من قائمة منسدلة (e.g., Original Article, Review Article, Case Report, Letter to Editor). اختر النوع الذي يتوافق مع بحثك ودليل المؤلفين.
        4.  **إدخال معلومات المخطوطة (Enter Manuscript Information):**
            *   **العنوان (Full Title):** انسخ والصق عنوان بحثك كاملاً.
            *   **العنوان المختصر (Short Title / Running Head):** إذا طُلب.
            *   **الملخص (Abstract):** انسخ والصق ملخص بحثك. تأكد من مطابقته لعدد الكلمات المسموح به.
            *   **الكلمات المفتاحية (Keywords):** أدخل الكلمات المفتاحية (عادة 3-7 كلمات)، قد يكون لكل كلمة حقل منفصل أو تُفصل بفواصل.
            *   **التصنيفات (Classifications/Categories):** بعض المجلات تطلب منك اختيار تصنيفات لموضوع بحثك من قائمة محددة.
        5.  **إضافة/تحرير المؤلفين (Add/Edit Authors):**
            *   أدخل معلومات جميع المؤلفين بالترتيب الصحيح: الاسم الكامل، البريد الإلكتروني (يفضل المؤسسي)، الانتماء المؤسسي الكامل (القسم، الكلية، الجامعة، المدينة، الدولة)، و ORCID ID إذا توفر.
            *   حدد المؤلف المراسل (Corresponding Author) بشكل واضح.
        6.  **تفاصيل إضافية (Additional Information / Questionnaire):**
            *   قد تُسأل أسئلة مثل:
                *   هل البحث جزء من أطروحة؟
                *   هل تم عرضه في مؤتمر؟ (إذا نعم، قد يُطلب تفاصيل).
                *   تأكيد الالتزام بأخلاقيات النشر.
                *   إقرارات حول تضارب المصالح، التمويل، الموافقة الأخلاقية، توفر البيانات (قد تكون إجابات بسيطة بنعم/لا مع الإشارة إلى الملفات المرفقة).
        7.  **اقتراح/استبعاد محكمين (Suggest / Oppose Reviewers) - (اختياري ولكن مفضل):**
            *   **اقتراح محكمين (Suggest Reviewers):** يمكنك اقتراح 3-5 خبراء في مجال بحثك لمراجعة المخطوطة. يجب أن يكونوا مستقلين (ليسوا من نفس مؤسستك، أو متعاونين حديثين، أو مشرفين سابقين). قدم أسماءهم، انتماءاتهم، وبريدهم الإلكتروني الرسمي، وسبب وجيه لاقتراحهم.
            *   **استبعاد محكمين (Oppose Reviewers):** إذا كان هناك أشخاص تعتقد أنهم قد يكونون متحيزين ضد عملك بشكل غير عادل، يمكنك طلب استبعادهم مع ذكر سبب مقنع (بهدوء وموضوعية).
        8.  **إرفاق الملفات (Attach/Upload Files):**
            *   هذه خطوة حاسمة. نظام رفع الملفات عادة يطلب منك تحديد **نوع كل ملف (Item Type)** من قائمة منسدلة، ثم رفع الملف.
            *   **أنواع الملفات الشائعة:**
                *   Cover Letter
                *   Manuscript (Blinded/Anonymous Version if required)
                *   Manuscript (Unblinded/With Author Details - if separate from blinded, or if blinding not required)
                *   Title Page
                *   Figure (لكل شكل ملف منفصل عادةً، أو حسب تعليمات المجلة)
                *   Table (لكل جدول ملف منفصل، أو مدمجة في نهاية المخطوطة)
                *   Supplementary Material (لكل مادة تكميلية ملف منفصل)
                *   Conflict of Interest Statement
                *   Author Contribution Statement
                *   Ethical Approval Documentation
                *   Data Availability Statement
                *   Response to Reviewers (في حالة إعادة الإرسال بعد المراجعة)
            *   **ترتيب الملفات (Order of Files):** النظام قد يرتبها تلقائياً أو يطلب منك ترتيبها حسب الأهمية (مثلاً، Cover Letter أولاً، ثم Title Page، ثم Manuscript).
            *   تأكد من تسمية ملفاتك بشكل واضح (e.g., CoverLetter.docx, Manuscript_Blinded.docx, Figure1.tiff, Table1.docx).
        9.  **بناء ملف PDF للموافقة (Build PDF for Approval / View Submission):**
            *   بعد رفع جميع الملفات، يقوم النظام عادةً بإنشاء ملف PDF مجمع واحد يحتوي على جميع الملفات التي رفعتها (أو معظمها) بالترتيب الذي حددته المجلة.
        10. **مراجعة ملف PDF والموافقة (Review PDF and Approve/Submit):**
            *   **هام جداً:** قم بتحميل ملف PDF هذا ومراجعته بدقة شديدة للتأكد من أن كل شيء صحيح: النص، الأشكال (هل تظهر بوضوح؟)، الجداول، الترتيب، عدم وجود معلومات تعريفية في المخطوطة المعماة، إلخ.
            *   إذا كان هناك أي خطأ، عد للخطوات السابقة وقم بتعديل الملفات المرفوعة أو المعلومات المدخلة.
            *   بعد التأكد من أن كل شيء مثالي، اضغط على زر الموافقة النهائي (Approve Submission / Submit / Finalize Submission).
        11. **تأكيد الإرسال (Submission Confirmation):**
            *   ستتلقى رسالة تأكيد عبر البريد الإلكتروني تحتوي على رقم المخطوطة (Manuscript ID أو Manuscript Number). احتفظ بهذا الرقم جيداً، فهو مرجعك للمتابعة والاستفسار.
            *   يمكنك أيضاً رؤية المخطوطة وحالتها في لوحة التحكم الخاصة بك في نظام المجلة.
        """)

	st.subheader("🖥️ محاكي مبسط لبعض حقول الإرسال")
	st.markdown("هذا مجرد تمثيل لبعض الحقول التي قد تصادفها، وليس نظام إرسال فعلي.")

	with st.form("submission_simulation"):
		st.text_input("عنوان البحث (Full Title)")
		st.text_area("الملخص (Abstract - 250 words max)")
		st.text_input("الكلمات المفتاحية (Keywords - comma separated)")

		st.write("**معلومات المؤلف المراسل:**")
		col_author1, col_author2 = st.columns(2)
		with col_author1:
			st.text_input("الاسم الأول (First Name)")
			st.text_input("اسم العائلة (Last Name)")
		with col_author2:
			st.text_input("البريد الإلكتروني (Email)")
			st.text_input("الانتماء المؤسسي (Affiliation)")

		st.file_uploader("ارفع المخطوطة الرئيسية (Upload Main Manuscript - .docx, .pdf)", type=['docx', 'pdf'])
		st.file_uploader("ارفع رسالة التغطية (Upload Cover Letter - .docx, .pdf)", type=['docx', 'pdf'])

		st.checkbox("أؤكد أن هذا البحث أصيل ولم يُنشر سابقاً.")
		st.checkbox("أؤكد أن جميع المؤلفين وافقوا على هذا الإرسال.")

		submitted_simulation = st.form_submit_button("إرسال (محاكاة)")
		if submitted_simulation:
			st.success("تم إرسال معلوماتك بنجاح (هذه محاكاة فقط).")
			st.balloons()
	st.markdown("---")
	st.info(
		"💡 نصيحة: قبل البدء في عملية الإرسال الفعلية، جهز جميع ملفاتك ومعلوماتك في مجلد واحد على حاسوبك لتسهيل العملية وتجنب الأخطاء.")

elif page == "⏳ المرحلة الخامسة: ما بعد الإرسال":
	st.markdown("<h1>⏳ المرحلة الخامسة: ما بعد الإرسال (Post-Submission)</h1>", unsafe_allow_html=True)
	st.markdown("""
    بمجرد إرسال مخطوطتك، تبدأ مرحلة الانتظار والمتابعة. فهم ما يحدث خلف الكواليس يمكن أن يساعد في تخفيف القلق.
    """)
	st.markdown("---")

	with st.expander("📊 تتبع حالة المخطوطة (Tracking Manuscript Status)"):
		st.markdown("""
        *   يمكنك متابعة حالة مخطوطتك عبر نظام الإرسال الإلكتروني للمجلة باستخدام حسابك (Author Dashboard).
        *   **الحالات الشائعة التي قد تراها (قد تختلف المسميات قليلاً بين المجلات):**
            *   **Submitted to Journal / Manuscript Received:** تم استلام البحث بنجاح.
            *   **With Editor / Editor Invited / Editor Assigned:** البحث مع أحد المحررين (عادةً محرر القسم أو مساعد محرر) لتقييم أولي (فحص الملاءمة، الجودة الأساسية، الالتزام بتعليمات المجلة).
            *   **Technical Check / Admin Check:** فحص إداري أو تقني للملفات والتنسيق.
            *   **Reviewers Invited:** تم دعوة المحكمين لمراجعة البحث.
            *   **Under Review:** وافق المحكمون على الدعوة والبحث قيد المراجعة من قبلهم.
            *   **Required Reviews Complete / All Reviews Received:** اكتملت عملية التحكيم، وتقارير المحكمين أصبحت لدى المحرر.
            *   **Decision in Process:** المحرر يراجع تقارير المحكمين ويتخذ قراراً. قد يستشير محررين آخرين أو رئيس التحرير.
            *   **Decision Letter Sent / Decision Made:** تم إرسال خطاب القرار لك عبر البريد الإلكتروني ويمكنك رؤيته في النظام.
        """)
		st.subheader("🔍 محاكي تتبع حالة المخطوط")
		manuscript_id_track = st.text_input("أدخل رقم مرجع المخطوط للمتابعة (مثال: JCS-2023-0123):", key="tracker_id")
		if manuscript_id_track:
			# Simulate status based on input (very basic simulation)
			if "0123" in manuscript_id_track:
				current_sim_status = "Under Review"
				date_sim_status = "2023-10-15"
			elif "0456" in manuscript_id_track:
				current_sim_status = "Decision in Process"
				date_sim_status = "2023-11-01"
			else:
				current_sim_status = "Submitted to Journal"
				date_sim_status = "2023-11-20"
			st.info(f"**حالة المخطوطة {manuscript_id_track}:** {current_sim_status} (آخر تحديث: {date_sim_status})")

			# Example timeline
			timeline_data_sim = [
				{"المرحلة": "تم الاستلام", "التاريخ": "2023-09-01", "ملاحظات": "تم استلام المخطوط بنجاح."},
				{"المرحلة": "مع المحرر", "التاريخ": "2023-09-03", "ملاحظات": "المخطوط قيد المراجعة الأولية."},
				{"المرحلة": "دعوة المحكمين", "التاريخ": "2023-09-10", "ملاحظات": "تم إرسال دعوات للمحكمين."},
				{"المرحلة": "تحت المراجعة", "التاريخ": "2023-09-15", "ملاحظات": "المخطوط قيد مراجعة الأقران."},
			]
			if current_sim_status == "Decision in Process":
				timeline_data_sim.append(
					{"المرحلة": "اكتملت المراجعات", "التاريخ": "2023-10-30", "ملاحظات": "تقارير المحكمين لدى المحرر."})
				timeline_data_sim.append(
					{"المرحلة": "القرار قيد الإعداد", "التاريخ": date_sim_status, "ملاحظات": "المحرر يتخذ القرار."})

			df_timeline_sim = pd.DataFrame(timeline_data_sim)
			st.table(df_timeline_sim.set_index("المرحلة"))

	with st.expander("📧 أنواع القرارات المحتملة (Potential Decision Types)"):
		st.markdown("""
        *   **الرفض المباشر (Desk Rejection / Reject without Review):** رفض البحث من قبل المحرر قبل إرساله للمحكمين. الأسباب الشائعة:
            *   خارج نطاق المجلة (Out of Scope).
            *   جودة منخفضة جداً أو مشاكل منهجية واضحة.
            *   عدم الالتزام بتعليمات المجلة بشكل كبير.
            *   مشاكل أخلاقية واضحة (مثل الانتحال).
            *   مساهمة علمية غير كافية أو غير أصيلة.
        *   **الرفض بعد التحكيم (Reject after Review):** البحث لا يرقى لمعايير النشر في المجلة بناءً على تقارير المحكمين. قد تكون هناك عيوب جوهرية في المنهجية، التحليل، أو الاستنتاجات.
        *   **تعديلات جذرية (Major Revisions / Revise and Resubmit):** البحث لديه إمكانية للنشر ولكن يتطلب تغييرات كبيرة وإضافات جوهرية لمعالجة ملاحظات المحكمين. ستحتاج لإعادة الإرسال مع رد مفصل على جميع التعليقات. قد يُرسل البحث المعدل لنفس المحكمين أو لمحكمين جدد.
        *   **تعديلات طفيفة (Minor Revisions):** البحث جيد بشكل عام ولكن يحتاج لتعديلات بسيطة (لغوية، توضيح نقاط معينة، تصحيح أخطاء صغيرة، إضافة مراجع). عادة ما يراجع المحرر هذه التعديلات بنفسه.
        *   **قبول مشروط (Conditional Accept / Accept pending Revisions):** قبول البحث بشرط إجراء التعديلات الطفيفة المطلوبة بشكل مُرضٍ.
        *   **قبول نهائي (Accept):** مبروك! تم قبول بحثك للنشر كما هو أو بعد تعديلات طفيفة جداً.
        """)

	with st.expander("📝 كيفية الرد على تعليقات المحكمين (Responding to Reviewer Comments)"):
		st.markdown("""
        استلام طلب تعديلات هو أمر شائع جداً وجزء طبيعي من عملية النشر. تعامل معه كفرصة لتحسين بحثك.
        *   **كن مهذباً ومحترفاً:** ابدأ رسالة الرد بشكر المحرر والمحكمين على وقتهم وجهدهم وملاحظاتهم القيمة.
        *   **رد على كل نقطة بالتفصيل:** قم بإنشاء مستند (Response to Reviewers / Rebuttal Letter) ترد فيه على كل تعليق من كل محكم على حدة. انسخ تعليق المحكم ثم اكتب ردك تحته.
        *   **وضح التغييرات:** اذكر بوضوح أين وكيف قمت بإجراء التعديلات في المخطوطة المعدلة (مثلاً، "لقد أضفنا شرحاً لهذه النقطة في الصفحة 5، الأسطر 10-12، الفقرة الثانية" أو "تم تعديل الجدول 2 ليشمل هذه المعلومات كما هو موضح في الصفحة 7").
        *   **استخدم تمييزاً للتعديلات:** في النسخة المعدلة من المخطوطة، استخدم لوناً مختلفاً للنص المضاف أو خاصية "Track Changes" في Word لتوضيح التعديلات التي أجريتها. هذا يسهل على المحرر والمحكمين مراجعة التغييرات. (تأكد من تعليمات المجلة حول هذا).
        *   **إذا لم توافق على نقطة ما:** اشرح وجهة نظرك بأدب وبأدلة علمية قوية. لا تكن دفاعياً بشكل مبالغ فيه. يمكنك أن تقول مثلاً: "نتفهم وجهة نظر المحكم، ولكننا نعتقد أن [...] للأسباب التالية: [...]. ومع ذلك، قمنا بإضافة توضيح في النص لمعالجة هذا القلق جزئياً في الصفحة X."
        *   **الالتزام بالمهلة الزمنية:** عادة ما تمنحك المجلة مهلة محددة لإجراء التعديلات وإعادة الإرسال. إذا كنت بحاجة لمزيد من الوقت، تواصل مع المحرر واطلب تمديداً مع ذكر السبب.
        *   **ملف الرد (Response to Reviewers Letter):** هذا ملف مهم جداً يتم رفعه مع المخطوطة المعدلة وملفاتها الأخرى.
        """)
		st.subheader("نموذج مبسط لخطاب الرد على المحكمين")
		st.code("""
[تاريخ اليوم]

إلى محرر مجلة [اسم المجلة]

الموضوع: رد على تعليقات المحكمين بخصوص المخطوطة رقم [رقم المخطوطة] بعنوان "[عنوان المخطوطة]"

السيد المحرر الكريم،

نشكركم جزيل الشكر على إتاحة الفرصة لنا لمراجعة مخطوطتنا بناءً على التعليقات البناءة التي قدمها المحكمون الكرام. لقد وجدنا هذه التعليقات مفيدة للغاية وساهمت في تحسين جودة عملنا بشكل كبير.

لقد قمنا بمعالجة جميع النقاط التي أثارها المحكمون، ونرفق طيه نسخة معدلة من المخطوطة (مع تمييز التعديلات) بالإضافة إلى رد مفصل على كل تعليق أدناه.

نتمنى أن تكون التعديلات التي أجريناها قد أرضت متطلباتكم وتطلعات المحكمين.

مع خالص التقدير،
[اسم المؤلف المراسل]
[الانتماء]

--------------------------------------------------
**الردود التفصيلية على تعليقات المحكمين:**

**المحكم 1:**

**التعليق 1.1:** [اكتب تعليق المحكم هنا كاملاً]
**الرد:** نشكر المحكم على هذه الملاحظة الهامة. لقد قمنا بـ [اشرح التعديل الذي قمت به]. يمكن الاطلاع على هذا التعديل في [اذكر رقم الصفحة، الفقرة، أو السطر في المخطوطة المعدلة].

**التعليق 1.2:** [اكتب تعليق المحكم هنا كاملاً]
**الرد:** نتفق مع المحكم في هذه النقطة. وعليه، فقد [اشرح التعديل]. هذا التعديل موجود في [اذكر الموقع].

**(إذا كنت لا توافق على تعليق ما):**
**التعليق 1.3:** [اكتب تعليق المحكم هنا كاملاً]
**الرد:** نقدر وجهة نظر المحكم. ومع ذلك، فإننا نعتقد أن [اشرح وجهة نظرك بأدب مع تقديم مبررات علمية]. لمزيد من التوضيح، أضفنا جملة في [اذكر الموقع] لتوضيح هذا الجانب.

**المحكم 2:**

**التعليق 2.1:** [اكتب تعليق المحكم هنا كاملاً]
**الرد:** شكراً للمحكم على هذا الاقتراح. لقد قمنا بـ [اشرح التعديل]، ويمكن العثور عليه في [اذكر الموقع].

[استمر بنفس الطريقة لجميع التعليقات من جميع المحكمين]
        """, language="text")

	with st.expander("🎉 القبول وما بعده (Acceptance and Beyond)"):
		st.markdown("""
        *   **رسالة القبول (Acceptance Letter):** ستتلقى رسالة رسمية بقبول بحثك. تهانينا!
        *   **التدقيق النهائي للنسخة قبل الطبع (Proofs / Galley Proofs):** سترسل لك المجلة نسخة من البحث بصيغته النهائية كما سيظهر عند النشر (عادةً ملف PDF) لمراجعتها بحثاً عن أي أخطاء مطبعية، تنسيقية، أو أخطاء في معلومات المؤلفين أو الأشكال والجداول. **راجعها بدقة شديدة!** هذه هي فرصتك الأخيرة لتصحيح الأخطاء الصغيرة. لا تقم بإجراء تغييرات كبيرة في المحتوى في هذه المرحلة.
        *   **نماذج نقل حقوق النشر (Copyright Transfer Agreement / License to Publish):** ستوقع اتفاقية إما لنقل حقوق النشر للمجلة (في المجلات التقليدية) أو لاختيار رخصة نشر مفتوح (Open Access license, e.g., Creative Commons) إذا كانت المجلة مفتوحة الوصول ودفعت رسوم النشر (APC) إذا كانت مطلوبة.
        *   **(إذا كانت مجلة وصول مفتوح برسوم) دفع رسوم معالجة المقال (APC - Article Processing Charge).**
        *   **النشر الإلكتروني المبكر (Online First / Early View / Ahead of Print):** قد يُنشر بحثك إلكترونياً على موقع المجلة قبل أن يُدرج في عدد ورقي أو إلكتروني محدد. هذا يجعله متاحاً للاطلاع والاقتباس بشكل أسرع.
        *   **النشر النهائي (Final Publication):** يتم نشر بحثك في عدد محدد من المجلة (مع رقم مجلد، عدد، وأرقام صفحات).
        *   **الاحتفال والمشاركة (Celebrate and Share):** بمجرد نشر بحثك، شاركه مع زملائك، عبر منصات التواصل الأكاديمي (مثل ResearchGate, Academia.edu, LinkedIn)، وفي سيرتك الذاتية، وعلى موقع مؤسستك.
        """)
	st.balloons()

elif page == "📊 إحصائيات ومؤشرات النشر":
	st.markdown("<h1>📊 إحصائيات ومؤشرات النشر العلمي</h1>", unsafe_allow_html=True)
	st.markdown("""
    فهم بعض الإحصائيات والمؤشرات المتعلقة بالنشر العلمي يمكن أن يساعدك في اتخاذ قرارات أفضل ووضع توقعات واقعية.
    """)
	st.markdown("---")

	# General Statistics
	col1, col2, col3 = st.columns(3)
	with col1:
		st.metric(label="متوسط وقت المراجعة التقديري", value="3-6 أشهر", delta="يختلف حسب المجلة والتخصص",
				  delta_color="off")
	with col2:
		st.metric(label="متوسط معدل القبول العام", value="~20-40%", delta="يتأثر بجودة المجلة والتخصص",
				  delta_color="off")
	with col3:
		st.metric(label="نمو مجلات الوصول المفتوح", value="متزايد", delta="خيارات نشر أوسع", delta_color="normal")

	st.markdown("---")
	st.subheader("📈 الاتجاهات السنوية في النشر (مثال توضيحي)")
	# Dummy data for trends
	years = list(range(2018, 2024))
	publications_trend = [1.2, 1.3, 1.35, 1.45, 1.55, 1.6]  # In millions (hypothetical)
	open_access_trend = [25, 28, 32, 35, 38, 42]  # Percentage (hypothetical)

	df_trends = pd.DataFrame({
		'السنة': years,
		'عدد الأبحاث المنشورة (بالملايين)': publications_trend,
		'نسبة الوصول المفتوح (%)': open_access_trend
	})

	fig_line_trends = px.line(df_trends, x='السنة', y=['عدد الأبحاث المنشورة (بالملايين)', 'نسبة الوصول المفتوح (%)'],
							  title="اتجاهات النشر العلمي عالمياً (بيانات افتراضية)",
							  labels={'value': 'القيمة', 'variable': 'المؤشر'})
	fig_line_trends.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
	st.plotly_chart(fig_line_trends, use_container_width=True)

	st.markdown("---")
	st.subheader("📊 توزيع النشر حسب التخصص (مثال توضيحي)")
	fields_data = {
		'التخصص': ["العلوم الطبية والصحية", "الهندسة والتكنولوجيا", "العلوم الطبيعية", "العلوم الاجتماعية",
				   "الإنسانيات والفنون"],
		'نسبة النشر (%)': [30, 25, 20, 15, 10]  # Hypothetical
	}
	df_fields = pd.DataFrame(fields_data)
	fig_pie_fields = px.pie(df_fields, values='نسبة النشر (%)', names='التخصص',
							title="توزيع الأبحاث المنشورة حسب التخصص (بيانات افتراضية)")
	fig_pie_fields.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
	st.plotly_chart(fig_pie_fields, use_container_width=True)

	st.markdown("---")
	st.subheader("📉 العوامل المؤثرة على قرارات النشر والرفض")
	rejection_factors = {
		'العامل': [
			"خارج نطاق المجلة (Out of Scope)",
			"مساهمة علمية غير كافية أو أصالة محدودة",
			"عيوب منهجية جوهرية",
			"تحليل بيانات غير سليم أو غير كافٍ",
			"استنتاجات غير مدعومة بالنتائج",
			"كتابة رديئة أو غير واضحة",
			"عدم الالتزام بإرشادات المجلة",
			"مشاكل أخلاقية (انتحال، تزوير بيانات)",
			"عدم كفاية مراجعة الأدبيات",
			"أهمية منخفضة لمجال البحث أو قراء المجلة"
		],
		'الأهمية النسبية': [
			"مرتفعة جداً (سبب رئيسي للرفض المباشر)",
			"مرتفعة جداً",
			"مرتفعة جداً",
			"مرتفعة",
			"مرتفعة",
			"متوسطة إلى مرتفعة",
			"متوسطة (قد تؤدي لرفض مباشر أو طلب تعديل)",
			"مرتفعة جداً (رفض مباشر)",
			"متوسطة",
			"متوسطة إلى مرتفعة"
		]
	}
	df_rejection = pd.DataFrame(rejection_factors)
	st.table(df_rejection.set_index("العامل"))
	st.markdown("---")
	st.markdown(
		"<div class='info-box'>ملاحظة: الإحصائيات والمؤشرات المعروضة هنا هي لأغراض توضيحية وقد لا تعكس بيانات دقيقة أو حديثة لجميع المجالات. يُنصح بالرجوع إلى مصادر متخصصة للحصول على أحدث المعلومات.</div>",
		unsafe_allow_html=True)


elif page == "📖 قاموس المصطلحات":
	st.markdown("<h1>📖 قاموس المصطلحات الهامة في النشر العلمي</h1>", unsafe_allow_html=True)
	st.markdown("""
    <div class='highlight-box'>
    فيما يلي قائمة بأهم المصطلحات المستخدمة في عملية النشر العلمي باللغتين العربية والإنجليزية مع شرح موجز.
    </div>
    """, unsafe_allow_html=True)

	terminology_data = [
		{"المصطلح بالعربية": "النشر العلمي", "المصطلح بالإنجليزية": "Scientific Publishing",
		 "الشرح": "عملية نشر الأبحاث والدراسات العلمية في المجلات المحكمة أو الكتب الأكاديمية."},
		{"المصطلح بالعربية": "المخطوطة", "المصطلح بالإنجليزية": "Manuscript",
		 "الشرح": "النسخة الأولية من البحث العلمي المقدم للنشر."},
		{"المصطلح بالعربية": "المجلة المحكمة / الدورية العلمية",
		 "المصطلح بالإنجليزية": "Peer-Reviewed Journal / Scientific Journal",
		 "الشرح": "مجلة علمية تخضع الأبحاث المقدمة إليها لعملية تحكيم (مراجعة الأقران) من قبل خبراء متخصصين في نفس المجال."},
		{"المصطلح بالعربية": "مراجعة الأقران / التحكيم", "المصطلح بالإنجليزية": "Peer Review",
		 "الشرح": "عملية تقييم البحث من قبل خبراء متخصصين (محكمين) في نفس مجال البحث لضمان جودته وأصالته قبل نشره."},
		{"المصطلح بالعربية": "المحكمون", "المصطلح بالإنجليزية": "Reviewers / Referees",
		 "الشرح": "الخبراء الذين يقومون بتقييم المخطوطات العلمية."},
		{"المصطلح بالعربية": "رئيس التحرير", "المصطلح بالإنجليزية": "Editor-in-Chief (EIC)",
		 "الشرح": "المسؤول الأعلى في هيئة تحرير المجلة، يتخذ القرارات النهائية بشأن النشر."},
		{"المصطلح بالعربية": "محرر القسم / المحرر المشارك", "المصطلح بالإنجليزية": "Section Editor / Associate Editor",
		 "الشرح": "محرر متخصص في جزء معين من نطاق المجلة، يدير عملية مراجعة المخطوطات في تخصصه."},
		{"المصطلح بالعربية": "رسالة التغطية", "المصطلح بالإنجليزية": "Cover Letter",
		 "الشرح": "رسالة رسمية موجهة لرئيس تحرير المجلة، تقدم البحث وتوضح أهميته وملاءمته للمجلة."},
		{"المصطلح بالعربية": "الملخص", "المصطلح بالإنجليزية": "Abstract",
		 "الشرح": "ملخص موجز وشامل للبحث (عادة 150-300 كلمة) يتضمن الخلفية، الأهداف، الطرق، النتائج الرئيسية، والاستنتاجات."},
		{"المصطلح بالعربية": "الكلمات المفتاحية", "المصطلح بالإنجليزية": "Keywords",
		 "الشرح": "مصطلحات رئيسية (عادة 3-7 كلمات) تصف محتوى البحث وتساعد في فهرسته وتسهيل العثور عليه."},
		{"المصطلح بالعربية": "المراجع", "المصطلح بالإنجليزية": "References / Bibliography",
		 "الشرح": "قائمة بجميع المصادر التي تم الاستشهاد بها في البحث، منسقة حسب أسلوب المجلة."},
		{"المصطلح بالعربية": "معامل التأثير", "المصطلح بالإنجليزية": "Impact Factor (IF)",
		 "الشرح": "مقياس لأهمية المجلة العلمية، يعكس متوسط عدد الاستشهادات السنوية للمقالات المنشورة في تلك المجلة خلال السنتين السابقتين."},
		{"المصطلح بالعربية": "التصنيف الربعي للمجلة", "المصطلح بالإنجليزية": "Journal Quartile (Q1, Q2, Q3, Q4)",
		 "الشرح": "تصنيف المجلات ضمن تخصصها إلى أربعة أرباع بناءً على معامل التأثير أو مؤشرات أخرى (Q1 هو الأعلى)."},
		{"المصطلح بالعربية": "الفهرسة", "المصطلح بالإنجليزية": "Indexing",
		 "الشرح": "إدراج المجلة في قواعد بيانات علمية عالمية موثوقة مثل Scopus, Web of Science (WoS), PubMed, Medline, ERIC، مما يزيد من رؤيتها ومصداقيتها."},
		{"المصطلح بالعربية": "الرفض المباشر / من المكتب",
		 "المصطلح بالإنجليزية": "Desk Rejection / Reject without Review",
		 "الشرح": "رفض المخطوطة من قبل المحرر قبل إرسالها للمحكمين، عادةً لعدم ملاءمتها لنطاق المجلة أو لضعف جودتها بشكل واضح."},
		{"المصطلح بالعربية": "تعديلات طفيفة", "المصطلح بالإنجليزية": "Minor Revisions",
		 "الشرح": "طلب إجراء تعديلات بسيطة على المخطوطة قبل قبولها للنشر."},
		{"المصطلح بالعربية": "تعديلات جذرية / كبرى", "المصطلح بالإنجليزية": "Major Revisions",
		 "الشرح": "طلب إجراء تغييرات كبيرة وجوهرية على المخطوطة، وقد تحتاج لإعادة تحكيم بعد التعديل."},
		{"المصطلح بالعربية": "القبول المشروط", "المصطلح بالإنجليزية": "Conditional Accept / Accept pending Revisions",
		 "الشرح": "قبول البحث بشرط إجراء التعديلات الطفيفة المطلوبة بشكل مُرضٍ."},
		{"المصطلح بالعربية": "القبول النهائي", "المصطلح بالإنجليزية": "Acceptance",
		 "الشرح": "قرار بقبول المخطوطة للنشر في المجلة."},
		{"المصطلح بالعربية": "النشر المفتوح / الوصول الحر", "المصطلح بالإنجليزية": "Open Access (OA)",
		 "الشرح": "نموذج نشر يتيح الوصول المجاني والفوري لمحتوى البحث العلمي لجميع القراء عبر الإنترنت دون قيود مالية أو قانونية كبيرة."},
		{"المصطلح بالعربية": "رسوم معالجة المقال", "المصطلح بالإنجليزية": "Article Processing Charge (APC)",
		 "الشرح": "رسوم يدفعها المؤلفون (أو مؤسساتهم/مموليهم) لجعل مقالهم متاحًا بنظام الوصول المفتوح في بعض المجلات."},
		{"المصطلح بالعربية": "المجلات المفترسة", "المصطلح بالإنجليزية": "Predatory Journals",
		 "الشرح": "مجلات تدعي أنها علمية ومحكمة ولكن هدفها الأساسي هو الربح المادي من رسوم النشر دون تقديم خدمات تحريرية أو تحكيم حقيقي."},
		{"المصطلح بالعربية": "الانتحال / السرقة الأدبية", "المصطلح بالإنجليزية": "Plagiarism",
		 "الشرح": "استخدام أفكار أو كلمات أو أعمال شخص آخر دون الإشارة إليه بشكل صحيح، ونسبتها إلى النفس."},
		{"المصطلح بالعربية": "تضارب المصالح", "المصطلح بالإنجليزية": "Conflict of Interest (COI)",
		 "الشرح": "حالة قد تؤثر فيها المصالح الشخصية أو المالية أو المهنية للمؤلف أو المحكم أو المحرر على موضوعية البحث أو قرارات النشر."},
		{"المصطلح بالعربية": "المؤلف المراسل", "المصطلح بالإنجليزية": "Corresponding Author",
		 "الشرح": "الباحث المسؤول عن التواصل مع المجلة خلال عملية تقديم ومراجعة ونشر البحث، وعادة ما يكون نقطة الاتصال للاستفسارات بعد النشر."},
		{"المصطلح بالعربية": "معرف ORCID", "المصطلح بالإنجليزية": "ORCID (Open Researcher and Contributor ID)",
		 "الشرح": "معرف رقمي فريد ودائم للباحثين، يساعد في تمييزهم وربطهم بمنشوراتهم وأنشطتهم البحثية."},
		{"المصطلح بالعربية": "المعرف الرقمي للكائن (للمقال)", "المصطلح بالإنجليزية": "Digital Object Identifier (DOI)",
		 "الشرح": "رمز تعريفي فريد ودائم للمقالات العلمية وغيرها من المحتويات الرقمية، يضمن الوصول إليها حتى لو تغير موقعها على الإنترنت."},
		{"المصطلح بالعربية": "النسخة قبل الطبع / المسودة النهائية للمؤلف",
		 "المصطلح بالإنجليزية": "Preprint / Author's Accepted Manuscript (AAM)",
		 "الشرح": "Preprint: نسخة من البحث قبل خضوعه لمراجعة الأقران. AAM: النسخة النهائية للمخطوطة بعد مراجعة الأقران وقبولها للنشر، ولكن قبل تنسيق المجلة النهائي."},
		{"المصطلح بالعربية": "النسخة النهائية قبل الطباعة (للمراجعة)", "المصطلح بالإنجليزية": "Proofs / Galley Proofs",
		 "الشرح": "النسخة المنسقة من المقال كما ستظهر في المجلة، تُرسل للمؤلف للمراجعة النهائية بحثاً عن الأخطاء المطبعية قبل النشر الفعلي."},
		{"المصطلح بالعربية": "حقوق النشر", "المصطلح بالإنجليزية": "Copyright",
		 "الشرح": "الحقوق القانونية التي تمنح المؤلف (أو الناشر بعد نقل الحقوق) السيطرة على استخدام وتوزيع عمله الإبداعي."},
		{"المصطلح بالعربية": "النشر الإلكتروني المبكر",
		 "المصطلح بالإنجليزية": "Online First / Early View / Ahead of Print",
		 "الشرح": "نشر المقال إلكترونيًا على موقع المجلة بعد قبوله وقبل إدراجه في عدد ورقي أو إلكتروني محدد، مما يسرع من إتاحته."},
	]

	df_terminology = pd.DataFrame(terminology_data)

	# Display as a styled table
	st.dataframe(df_terminology.style.set_properties(**{'text-align': 'right'}), use_container_width=True, height=600)

# Alternative display using expanders for each term for more space if needed
# for item in terminology_data:
#     with st.expander(f"{item['المصطلح بالعربية']} ({item['المصطلح بالإنجليزية']})"):
#         st.write(item['الشرح'])

# --- Footer ---
st.markdown("---")
st.markdown(
	"""
	<p style="text-align:center; color: #555;">
	نتمنى أن يكون هذا الدليل مفيداً في رحلتكم نحو النشر العلمي الدولي. بالتوفيق! 🌟
	<br>
	© دليل النشر العلمي التفاعلي
	</p>
	""", unsafe_allow_html=True
)