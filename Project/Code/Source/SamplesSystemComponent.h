
#pragma once

#include <AzCore/Component/Component.h>

#include <Samples/SamplesBus.h>

namespace Samples
{
    class SamplesSystemComponent
        : public AZ::Component
        , protected SamplesRequestBus::Handler
    {
    public:
        AZ_COMPONENT(SamplesSystemComponent, "{7eb762c3-ddd6-472d-a5bf-a8bab6208122}");

        static void Reflect(AZ::ReflectContext* context);

        static void GetProvidedServices(AZ::ComponentDescriptor::DependencyArrayType& provided);
        static void GetIncompatibleServices(AZ::ComponentDescriptor::DependencyArrayType& incompatible);
        static void GetRequiredServices(AZ::ComponentDescriptor::DependencyArrayType& required);
        static void GetDependentServices(AZ::ComponentDescriptor::DependencyArrayType& dependent);

    protected:
        ////////////////////////////////////////////////////////////////////////
        // SamplesRequestBus interface implementation

        ////////////////////////////////////////////////////////////////////////

        ////////////////////////////////////////////////////////////////////////
        // AZ::Component interface implementation
        void Init() override;
        void Activate() override;
        void Deactivate() override;
        ////////////////////////////////////////////////////////////////////////
    };
}
